import csv, itertools

events = []
players = []
exp = []
attended_prev = []
multiplier = []

with open('input', 'r') as attendance_list:
	an_event = csv.reader(attendance_list, delimiter=',')

	for line in an_event:
		events.append(line)

	attendance_list.close()

count = 1
for event in events:
	
	#print(event)

	for player_name in itertools.islice(event,1,len(event)):

		if player_name not in players:
			players.append(player_name)
			exp.extend([0])
			multiplier.extend([0])
			attended_prev.extend([0])
			multiplier[players.index(player_name)] = 1.0

		if count > 1:
			if player_name in events[count-2]:
				attended_prev[players.index(player_name)] = 'yes'
				multiplier[players.index(player_name)] += 0.05
				#print(player_name + ' attended. Multiplier now at ' + str(multiplier[players.index(player_name)]))
				#print(str(100 * multiplier[players.index(player_name)]) + ' added to score')
			else:
				attended_prev[players.index(player_name)] = 'no'
				if multiplier[players.index(player_name)] > 1.0:
					multiplier[players.index(player_name)] -= 0.1

		exp[players.index(player_name)] += int(100 * multiplier[players.index(player_name)])

	count += 1

for i in range(len(players)):
	print(players[i] + ': ' + str(exp[i]) + 'XP')
