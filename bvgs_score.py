import csv, itertools

events = []
players = []
exp = []
attended_prev = []
multiplier = []

print('getting list...')
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
	print(players[i] + ': ' + str(exp[i]))

print(players)
print(exp)

'''
def menu():
	menu_choose = input(
		'BVGS Scorelist\n'
		+ '\n1. View player list'
		+ '\n2. View previous meetups'
		+ '\n3. Edit player list'
		+ '\n4. Log meeting'
		+ '\n>')
	if '1' in menu_choose:
		print(players)
		print('\n\n')
		menu()
	elif '2' in menu_choose:
		print(events)
		print('\n\n')
		menu()
	elif '3' in menu_choose:
		print('\n\n')
		player_edit()
	elif '4' in menu_choose:
		print('\n\n')
		log_meeting()

def player_edit():
	player_edit_in = input('== PLAYERS ==\n\n1. Add player\n2. Remove player\n>')

	if '1' in player_edit_in:
		add_player = input('Enter player name: ')
		if len(add_player) > 0:
			players.append(add_player)
			print(add_player + ' added to list.')
			print('\n\n')
			menu()
		else:
			print('Please enter a valid name.\n\n')
			player_edit()

def log_meeting():
	this_event = []
	enter_date = input('Enter date of meeting: ')
	if len(enter_date) > 0:
		this_event.append(enter_date)
		event_num = len(events)
		#debug
		print(event_num)
	else:
		print('\n')
		log_meeting()

	attendee = input('Enter attendee name; \'end\' to finish: ')

	if 'end' not in attendee:
		if attendee not in players:
			players.append(attendee)
		this_event.append(attendee)
	else:
		print('There must be at least one attendee!')
		menu()

	
	while 'end' not in attendee:
		print('Added.\n')

		attendee = list(input('Enter attendee name; \'end\' to finish: '))
		attLower[:] = attendee.lower()
		attFormatted = attLower[0].upper() + attLower[1:]
		if attFormatted not in players and 'end' not in attFormatted:
			players.append(attFormatted)

		if 'end' not in attFormatted:
			this_event.append(attFormatted)

	events.append(this_event)
	menu()

#def add_attendee():


menu()



	

#players.append('Ogre')

'''