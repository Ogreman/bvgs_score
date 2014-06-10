import csv, itertools

LEVELS = list(range(1, 25))
PLAYERS = dict()
BASE_EXP = 100

class ExpError(Exception):
	pass


class Player(object):

	def __init__(self, name):
		self.name = name
		self.multiplier = 1.0
		self.exp = 0
		self.level = 0
		self.req_exp = 0

	def attend_event(self):
		self.exp += self.next_amount

	def increase_multiplier(self):
		self.multiplier *= 1.1

	def check_level(self, exp_table):
		for level, exp in enumerate(exp_table):
			self.req_exp = exp - self.exp
			if exp > self.exp:
				self.level = level
				break
		return self.level

	@property
	def next_amount(self):
		return int(BASE_EXP * self.multiplier)

	def __str__(self):
		return self.name


def get_exp_table():
	exp_table = [BASE_EXP]
	for i in LEVELS:
		exp_table.append(int(exp_table[i-1] + BASE_EXP * (i / 1.5)))
	return exp_table


def read_events(input='input'):
	with open('input', 'r') as attendance_list:
		events = [line for line in csv.reader(attendance_list, delimiter=',')]
	return events


def check_attendance(events):
	for count, event in enumerate(events):
		for player_name in itertools.islice(event, 1, len(event)):
			player_name = player_name.strip()
			if player_name not in PLAYERS:
				PLAYERS[player_name] = Player(player_name)
			if player_name in events[count - 1]:
				PLAYERS[player_name].increase_multiplier()
			PLAYERS[player_name].attend_event()


if __name__ == '__main__':
	exp_table = get_exp_table()
	print('Levels: {}'.format(LEVELS))
	print('Total EXP needed: {}'.format(exp_table))
	events = read_events()
	check_attendance(events)

	print('\nSCORES:')

	for player in sorted(PLAYERS.values(), key=lambda x: x.check_level(exp_table)):
		print('{player}: Level {player.level} - {player.exp}XP - (to next: {player.req_exp}XP) -- Attending next event will earn {player.next_amount}XP!'.format(player=player))
