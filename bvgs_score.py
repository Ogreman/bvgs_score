import csv, itertools

events = []
players = []
exp = []
multiplier = []

levels = []
exp_table = []

exp_table.append(100)
for i in range(1,25):
	levels.append(i)
	exp_table.append(int(exp_table[i-1]+(100*(i/1.5))))
	#print(exp_table[i] - exp_table[i-1])

print('Levels:')
print(levels)
print('Total EXP needed:')
print(exp_table)


with open('input', 'r') as attendance_list:
	an_event = csv.reader(attendance_list, delimiter=',')

	for line in an_event:
		events.append(line)



count = 1
for event in events:
	
	#print(event)

	for player_name in itertools.islice(event,1,len(event)):
		player_name = player_name.strip()

		if player_name not in players:
			players.append(player_name)
			exp.extend([0])
			multiplier.extend([0])
			multiplier[players.index(player_name)] = 1.0

		if player_name in events[count-2]:
			multiplier[players.index(player_name)] *= 1.1

		exp[players.index(player_name)] += int(100 * multiplier[players.index(player_name)])

	count += 1

print('\nSCORES:')
for i in range(len(players)):
	current_player = players[i]
	current_exp = exp[i]
	current_multiplier = round(multiplier[i],2)

	j = 0
	while True:
		if exp_table[j] > exp[i]:
			current_level = levels[j-1]
			to_next_level = exp_table[j] - exp[i]
			break
		j += 1


	print(current_player + ': Level ' + str(current_level) + ' - ' + str(current_exp)
		+ 'XP - (to next: ' + str(to_next_level) + 'XP)'
		+ ' -- Attending next event will earn ' 
		+ str(int(100 * (multiplier[players.index(current_player)] * 1.1))) + ' XP!')
