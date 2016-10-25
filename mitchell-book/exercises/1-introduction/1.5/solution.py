"""
This is my attempt at creating a python script to complete the
following exercise from Mitchell's excellent book on machine
learning:

Implement an algorithm similar to that discussed for the
checkers problem, but use the simpler game of tic-tac-toe.

Represent the learned function V as a linear combination of
board features of your choice.

To train your program, play it repeatedly against a second
copy of the program that uses a fixed evaluation function
you create by hand.

Plot the percent of games won by your system, versus the
number of training games played.
"""

import random

############## Board Functions

def create_tic_tac_toe_board(x_positions=[], o_positions=[]):
	"""
	Creates a tic-tac-toe board with the given set of
	already played positions.
	"""
	board = [
		[' ', ' ', ' '],
		[' ', ' ', ' '],
		[' ', ' ', ' '],
	]

	for position in x_positions:
		row = position[0] - 1
		column = position[1] - 1
		board[row][column] = 'x'

	for position in o_positions:
		row = position[0] - 1
		column = position[1] - 1
		board[row][column] = 'o'

	return board

def create_board_from_existing_board(existing_board):
	board = [
		[' ', ' ', ' '],
		[' ', ' ', ' '],
		[' ', ' ', ' '],
	]
	for i in range(len(board)):
		for j in range(len(board[i])):
			board[i][j] = existing_board[i][j]

	return board

def determine_victory_condition(board):
	sets = parse_all_three_cell_sets_from_board(board)
	empty_positions = 0
	for _set in sets:
		if len(_set['x']) == 3:
			return True, 'x'
		if len(_set['o']) == 3:
			return True, 'o'
		empty_positions = empty_positions + len(_set['empty'])

	if empty_positions == 0:
		return True, ' '

	return False, None

def parse_all_three_cell_sets_from_board(board):
	sets = [
		[(1, 1), (1, 2), (1, 3)],
		[(2, 1), (2, 2), (2, 3)],
		[(3, 1), (3, 2), (3, 3)],
		[(1, 1), (2, 1), (3, 1)],
		[(1, 2), (2, 2), (3, 2)],
		[(1, 3), (2, 3), (3, 3)],
		[(1, 1), (2, 2), (3, 3)],
		[(1, 3), (2, 2), (3, 1)],
	]
	parsed_sets = []

	for _set in sets:
		empty_positions = []
		x_positions = []
		o_positions = []
		for position in _set:
			row = position[0] - 1
			column = position[1] - 1
			_type = board[row][column]
			if _type == ' ':
				empty_positions.append(position)
			elif _type == 'x':
				x_positions.append(position)
			elif _type == 'o':
				o_positions.append(position)

		parsed_sets.append({
			'empty': empty_positions,
			'x': x_positions,
			'o': o_positions,
		})

	return parsed_sets

def make_move(board, position, _type):
	"""
	Add a move to the board.
	"""

	if _type not in ['x', 'o']:
		raise ValueError("Must place an x or o")

	new_board = create_board_from_existing_board(board)

	row = position[0] - 1
	column = position[1] - 1

	new_board[row][column] = _type

	return new_board

def print_board(board):
	def print_vertical_bars(numbers):
		print(' ' + numbers[0] + ' | ' + numbers[1] + ' | ' + numbers[2] + ' ')

	def print_horizontal_line():
		print('-----------')

	for index in range(3):
			row = board[index]
			print_vertical_bars(row)
			if index != 2:
				print_horizontal_line()

############## Simple Static Strategy

def pick_move_by_simple_strategy(board, _type):
	if _type not in ['x', 'o']:
		raise ValueError("Must place an x or o")

	is_x = _type == 'x'
	sets = parse_all_three_cell_sets_from_board(board)

	# First check for obvious winning moves.

	for _set in sets:
		num_empty_positions = len(_set['empty'])
		num_x_positions = len(_set['x'])
		num_o_positions = len(_set['o'])

		# Case 1 - Winning move.
		if is_x and num_empty_positions == 1 and num_x_positions == 2:
			return _set['empty'][0]
		if not is_x and num_empty_positions == 1 and num_o_positions == 2:
			return _set['empty'][0]

		# Case 2 - Block Winning move.
		if is_x and num_empty_positions == 1 and num_o_positions == 2:
			return _set['empty'][0]
		if not is_x and num_empty_positions == 1 and num_x_positions == 2:
			return _set['empty'][0]

	# No obvious winning move discovered, so we'll pick a move in some set

	for _set in sets:
		num_empty_positions = len(_set['empty'])
		num_x_positions = len(_set['x'])
		num_o_positions = len(_set['o'])
		# Case 1 - Pick first position of set with some of our type already
		if is_x and num_empty_positions > 0 and num_x_positions > 0:
			return _set['empty'][0]
		if not is_x and num_empty_positions > 0 and num_o_positions > 0:
			return _set['empty'][0]

		# Case 2 - Find some empty position to return:
		if num_empty_positions > 0:
			return _set['empty'][0]

	raise ValueError("SOMEHOW WE DID NOT PICK ANYTHING")

############## ML Stuff below

def count_empty_sets(sets):
	empty_set_count = 0
	for _set in sets:
		if len(_set['empty']) == 3:
			empty_set_count = empty_set_count + 1
	return empty_set_count

def count_winning_sets(sets, is_x):
	winning_set_count = 0
	for _set in sets:
		num_empty_positions = len(_set['empty'])
		num_x_positions = len(_set['x'])
		num_o_positions = len(_set['o'])
		if is_x and num_x_positions == 3:
			winning_set_count = winning_set_count + 1
		if not is_x and num_o_positions == 3:
			winning_set_count = winning_set_count + 1
	return winning_set_count

def count_losing_sets(sets, is_x):
	losing_set_count = 0
	for _set in sets:
		num_empty_positions = len(_set['empty'])
		num_x_positions = len(_set['x'])
		num_o_positions = len(_set['o'])
		if is_x and num_o_positions == 3:
			losing_set_count = losing_set_count + 1
		if not is_x and num_x_positions == 3:
			losing_set_count = losing_set_count + 1
	return losing_set_count

def count_almost_winning_sets(sets, is_x):
	almost_winning_set_count = 0
	for _set in sets:
		num_empty_positions = len(_set['empty'])
		num_x_positions = len(_set['x'])
		num_o_positions = len(_set['o'])
		if is_x and num_empty_positions == 1 and num_x_positions == 2:
			almost_winning_set_count = almost_winning_set_count + 1
		if not is_x and num_empty_positions == 1 and num_o_positions == 2:
			almost_winning_set_count = almost_winning_set_count + 1
	return almost_winning_set_count

def count_almost_losing_sets(sets, is_x):
	almost_losing_set_count = 0
	for _set in sets:
		num_empty_positions = len(_set['empty'])
		num_x_positions = len(_set['x'])
		num_o_positions = len(_set['o'])
		if is_x and num_empty_positions == 1 and num_o_positions == 2:
			almost_losing_set_count = almost_losing_set_count + 1
		if not is_x and num_empty_positions == 1 and num_x_positions == 2:
			almost_losing_set_count = almost_losing_set_count + 1
	return almost_losing_set_count

def count_contended_sets(sets, is_x):
	contended_set_count = 0
	for _set in sets:
		num_empty_positions = len(_set['empty'])
		num_x_positions = len(_set['x'])
		num_o_positions = len(_set['o'])
		if num_empty_positions == 1 and num_x_positions == 1 and num_o_positions == 1:
			contended_set_count = contended_set_count + 1
	return contended_set_count

def count_irrelevant_sets(sets, is_x):
	irrelevant_set_count = 0
	for _set in sets:
		num_empty_positions = len(_set['empty'])
		num_x_positions = len(_set['x'])
		num_o_positions = len(_set['o'])
		if num_empty_positions == 0 and num_o_positions == 2 and num_x_positions == 1:
			irrelevant_set_count = irrelevant_set_count + 1
		if num_empty_positions == 0 and num_x_positions == 2 and num_o_positions == 1:
			irrelevant_set_count = irrelevant_set_count + 1
	return irrelevant_set_count

def count_opponent_only_sets(sets, is_x):
	opponent_only_set_count = 0
	for _set in sets:
		num_empty_positions = len(_set['empty'])
		num_x_positions = len(_set['x'])
		num_o_positions = len(_set['o'])
		if is_x and num_x_positions == 0 and num_o_positions > 0:
			opponent_only_set_count = opponent_only_set_count + 1
		if not is_x and num_o_positions == 0 and num_x_positions > 0:
			opponent_only_set_count = opponent_only_set_count + 1
	return opponent_only_set_count

def count_me_only_sets(sets, is_x):
	me_only_set_count = 0
	for _set in sets:
		num_empty_positions = len(_set['empty'])
		num_x_positions = len(_set['x'])
		num_o_positions = len(_set['o'])
		if is_x and num_o_positions == 0 and num_x_positions > 0:
			me_only_set_count = me_only_set_count + 1
		if not is_x and num_x_positions == 0 and num_o_positions > 0:
			me_only_set_count = me_only_set_count + 1
	return me_only_set_count

def count_xs(board):
	xs = 0
	for row in board:
		for column in row:
			if column == 'x':
				xs = xs +1
	return xs

def count_os(board):
	os = 0
	for row in board:
		for column in row:
			if column == 'o':
				os = os +1
	return os

def count_blanks(board):
	blanks = 0
	for row in board:
		for column in row:
			if column == ' ':
				blanks = blanks +1
	return blanks

def atomic_value(position, _type):
	if position == ' ':
		return 0
	elif position == _type:
		return 100
	else:
		return -100

def estimate_value_by_hypothesis(board, weights, _type):
	if len(weights) != 22:
		raise ValueError("Need 22 weights")

	is_x = _type == 'x'
	sets = parse_all_three_cell_sets_from_board(board)

	empty_sets = count_empty_sets(sets)
	winning_sets = count_winning_sets(sets, is_x)
	losing_sets = count_losing_sets(sets, is_x)
	almost_winning_sets = count_almost_winning_sets(sets, is_x)
	almost_losing_sets = count_almost_losing_sets(sets, is_x)
	contended_sets = count_contended_sets(sets, is_x)
	irrelevant_sets = count_irrelevant_sets(sets, is_x)
	sets_containing_only_opponents_pieces = count_opponent_only_sets(sets, is_x)
	sets_containing_only_my_pieces = count_me_only_sets(sets, is_x)
	number_of_xs = count_xs(board)
	number_of_os = count_os(board)
	number_of_blanks = count_blanks(board)
	position_1_1_value = atomic_value(board[0][0], _type)
	position_1_2_value = atomic_value(board[0][1], _type)
	position_1_3_value = atomic_value(board[0][2], _type)
	position_2_1_value = atomic_value(board[1][0], _type)
	position_2_2_value = atomic_value(board[1][1], _type)
	position_2_3_value = atomic_value(board[1][2], _type)
	position_3_1_value = atomic_value(board[2][0], _type)
	position_3_2_value = atomic_value(board[2][1], _type)
	position_3_3_value = atomic_value(board[2][2], _type)

	return sum([
		weights[0],
		weights[1] * empty_sets,
		weights[2] * winning_sets,
		weights[3] * losing_sets,
		weights[4] * almost_winning_sets,
		weights[5] * almost_losing_sets,
		weights[6] * contended_sets,
		weights[7] * irrelevant_sets,
		weights[8] * sets_containing_only_opponents_pieces,
		weights[9] * sets_containing_only_my_pieces,
		weights[10] * number_of_xs,
		weights[11] * number_of_os,
		weights[12] * number_of_blanks,
		weights[13] * position_1_1_value,
		weights[14] * position_1_2_value,
		weights[15] * position_1_3_value,
		weights[16] * position_2_1_value,
		weights[17] * position_2_2_value,
		weights[18] * position_2_3_value,
		weights[19] * position_3_1_value,
		weights[20] * position_3_2_value,
		weights[21] * position_3_3_value,
	])

def choose_move(board, weights, _type):
	empty_positions = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == ' ':
				empty_positions.append((i+1, j+1))

	best_move = None
	best_move_board_value = 0
	for position in empty_positions:
		proposed_board = make_move(board, position, _type)
		proposed_value = estimate_value_by_hypothesis(proposed_board, weights, _type)
		if proposed_value >= best_move_board_value:
			best_move = position
			best_move_board_value = proposed_value
	if not best_move:
		best_move = empty_positions[random.randint(0, len(empty_positions) - 1)]
		# best_move = empty_positions[0]

	return best_move

def run_performance(weights, _type):
	trace_boards = []
	winner = None

	board = create_tic_tac_toe_board()
	trace_boards.append(board)
	is_x_turn = True
	victory = False
	if _type == 'x':
		opponent = 'o'
	else:
		opponent = 'x'

	turns = 0
	while not victory:
		if is_x_turn and _type == 'x' or (not is_x_turn and _type == 'o'):
			# print()
			# print('It is x turn')
			# print_board(board)
			# move = pick_move_by_simple_strategy(board, opponent)
			move = choose_move(board, weights, _type)
			board = make_move(board, move, _type)
			is_x_turn = not is_x_turn
		else:
			# print()
			# print('It is o turn')
			# print_board(board)
			move = pick_move_by_simple_strategy(board, opponent)
			board = make_move(board, move, opponent)
			is_x_turn = not is_x_turn

		victory, victor = determine_victory_condition(board)
		if victory:
			winner = victor

		trace_boards.append(board)

	# print("victory")
	# print_board(board)

	return trace_boards, winner

def create_training_examples_from_trace(board_trace, weights, _type, rewards):
	examples = []
	for i in range(len(board_trace)):
		board = board_trace[i]
		was_victory, victor = determine_victory_condition(board)
		if was_victory:
			if victor == ' ':
				# We had a draw
				examples.append((board, rewards['draw']))

			if victor == _type:
				# We won
				examples.append((board, rewards['win']))
			else:
				# We lost
				examples.append((board, rewards['loss']))
		else:
			next_board_index = i + 2
			if next_board_index >= len(board_trace):
				next_board_index = i + 1
				if next_board_index >= len(board_trace):
					next_board_index = i
			next_board = board_trace[next_board_index]
			examples.append((board, estimate_value_by_hypothesis(board, weights, _type)))
	return examples

def generalize_examples_into_new_weights(examples, weights, _type):
	training_constant = 0.0000001
	new_weights = [weight for weight in weights]

	for board, value in examples:
		is_x = _type == 'x'
		sets = parse_all_three_cell_sets_from_board(board)

		empty_sets = count_empty_sets(sets)
		winning_sets = count_winning_sets(sets, is_x)
		losing_sets = count_losing_sets(sets, is_x)
		almost_winning_sets = count_almost_winning_sets(sets, is_x)
		almost_losing_sets = count_almost_losing_sets(sets, is_x)
		contended_sets = count_contended_sets(sets, is_x)
		irrelevant_sets = count_irrelevant_sets(sets, is_x)
		sets_containing_only_opponents_pieces = count_opponent_only_sets(sets, is_x)
		sets_containing_only_my_pieces = count_me_only_sets(sets, is_x)
		number_of_xs = count_xs(board)
		number_of_os = count_os(board)
		number_of_blanks = count_blanks(board)
		position_1_1_value = atomic_value(board[0][0], _type)
		position_1_2_value = atomic_value(board[0][1], _type)
		position_1_3_value = atomic_value(board[0][2], _type)
		position_2_1_value = atomic_value(board[1][0], _type)
		position_2_2_value = atomic_value(board[1][1], _type)
		position_2_3_value = atomic_value(board[1][2], _type)
		position_3_1_value = atomic_value(board[2][0], _type)
		position_3_2_value = atomic_value(board[2][1], _type)
		position_3_3_value = atomic_value(board[2][2], _type)

		# Update weights

		new_weights[0] = new_weights[0] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type))
		new_weights[1] = new_weights[1] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * empty_sets
		new_weights[2] = new_weights[2] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * winning_sets
		new_weights[3] = new_weights[3] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * losing_sets
		new_weights[4] = new_weights[4] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * almost_winning_sets
		new_weights[5] = new_weights[5] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * almost_losing_sets
		new_weights[6] = new_weights[6] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * contended_sets
		new_weights[7] = new_weights[7] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * irrelevant_sets
		new_weights[8] = new_weights[8] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * sets_containing_only_opponents_pieces
		new_weights[9] = new_weights[9] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * sets_containing_only_my_pieces
		new_weights[10] = new_weights[10] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * number_of_xs
		new_weights[11] = new_weights[11] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * number_of_os
		new_weights[12] = new_weights[12] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * number_of_blanks

		new_weights[13] = new_weights[13] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * position_1_1_value
		new_weights[14] = new_weights[14] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * position_1_2_value
		new_weights[15] = new_weights[15] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * position_1_3_value
		new_weights[16] = new_weights[16] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * position_2_1_value
		new_weights[17] = new_weights[17] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * position_2_2_value
		new_weights[18] = new_weights[18] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * position_2_3_value
		new_weights[19] = new_weights[19] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * position_3_1_value
		new_weights[20] = new_weights[20] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * position_3_2_value
		new_weights[21] = new_weights[21] + training_constant * (value - estimate_value_by_hypothesis(board, weights, _type)) * position_3_3_value

	return new_weights

############## Main Loop

weights = [
	0.002072306341060332,
	0.0012080644312910758,
	0.0055409784646103,
	-0.002425191566942204,
	0.0003917218081832788,
	0.0006802821854087128,
	0.005642334855468521,
	0.00615617913686461,
	0.0012000358914464888,
	0.002371836413411961,
	0.007777832930232056,
	0.0087695022797556,
	0.0021034218595553295,
	-0.05730113986651514,
	-0.13553814571049153,
	0.17616325691921286,
	-0.09443045463242464,
	0.1591895754187256,
	0.014618239330794253,
	0.1610134934043951,
	0.18112438273988174,
	-0.12857107567907597,
 ]

# weights = [0.0] * 22
_type = 'o'
opponent = 'x'
rewards = {
	'draw': 10,
	'win': 100,
	'loss': -10,
}

our_wins = 0
their_wins = 0
draws = 0
total_games = 0

while True:
	if total_games % 2 == 0:
		# total_games = 0
		# our_wins = 0
		# their_wins = 0
		# draws = 0
		if bool(random.getrandbits(1)):
			_type = 'o'
			opponent = 'x'
		else:
			_type = 'x'
			opponent = 'o'

	trace, winner = run_performance(weights, _type)
	total_games = total_games + 1
	if _type == winner:
		our_wins = our_wins + 1
	if opponent == winner:
		their_wins = their_wins + 1
	if ' ' == winner:
		draws = draws + 1

	examples = create_training_examples_from_trace(trace, weights, _type, rewards)
	weights = generalize_examples_into_new_weights(examples, weights, _type)

	percent_winning = our_wins / total_games
	their_percent_winning = their_wins / total_games
	draw_percentage = draws / total_games
	print("our win rate", percent_winning * 100)
	print("their win rate", their_percent_winning * 100)
	print("draw rate", draw_percentage * 100)
	print(weights)
	# if percent_winning * 100 > 99.5:
	# 	print("We've acheived a 99.5% win rate, so we'll quit now.")
	# 	break





















