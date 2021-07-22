from random import randrange

from search_problems import Node, Problem, a_star_search, greedy_first_search


class Puzzle(Problem):
	"""
	The values of the state member variables of instances of this class are
	represented as a string as follows:

	"12345678_" where '_' represents the empty tile.

	The inital state of the Puzzle problem is completely random.
	"""

	def actions(self, state):
		"""
		Actions labeled with 'U', 'D', 'L' or 'R' indicate the direction taken
		by the blank space.

		eg: +-------+      +-------+
			| _ 2 3 |      | 1 2 3 |
			| 1 4 6 | -D-> | _ 4 6 |
			| 7 5 8 |      | 7 5 8 |
			+-------+      +-------+
		"""
		actions = []
		index = state.index('_')
		if int(index / 3) > 0:
			# "move up allowed"
			actions.append('U')

		if int(index / 3) < 2:
			# "move down allowed"
			actions.append('D')

		if index % 3 > 0:
			# "move left allowed"
			actions.append('L')

		if index % 3 < 2:
			# "move right allowed"
			actions.append('R')

		return actions

	def is_goal(self, state):
		"""
		Return True if the problem is solved.  I.e.: human and all items are on
		the right side.
		"""
		return state == '12345678_'

	def transition(self, state, action):
		"""
		Paths labeled with 'U', 'D', 'L' or 'R' indicate the direction taken by the
		blank space.

		eg: +-------+      +-------+
			| _ 2 3 |      | 1 2 3 |
			| 1 4 6 | -D-> | _ 4 6 |
			| 7 5 8 |      | 7 5 8 |
			+-------+      +-------+
		"""
		index = state.index('_')
		if action == 'U':
			# "move up"
			new_state = list(state)
			new_state[index - 3], new_state[index] = new_state[index], \
			                                         new_state[index - 3]
			return ''.join(new_state)

		if action == 'D':
			# "move down"
			new_state = list(state)
			new_state[index + 3], new_state[index] = new_state[index], \
			                                         new_state[index + 3]
			return ''.join(new_state)

		if action == 'L':
			# "move left"
			new_state = list(state)
			new_state[index - 1], new_state[index] = new_state[index], \
			                                         new_state[index - 1]
			return ''.join(new_state)

		if action == 'R':
			# "move right"
			new_state = list(state)
			new_state[index + 1], new_state[index] = new_state[index], \
			                                         new_state[index + 1]
			return ''.join(new_state)


def misplaced_tiles_heuristic(node: Node) -> int:
	"""
	Return the heuristic value of a given node. The heuristic will count how
	many tiles are not in their designated position which indicates a minimum
	number of moves needed to solve the problem.

	:param node: Node
	:return: int
	"""
	heuristic = -1
	for (e, i) in zip(node.state, '12345678*'):
		heuristic += int(e == i)
	return heuristic


def print_puzzle(s):
	print(f"+-------+\n| {s[0]} {s[1]} {s[2]} |\n| {s[3]} {s[4]} {s[5]} |\n| {s[6]} {s[7]} {s[8]} |\n+-------+")


def generate_random_board():
	tiles = []
	state = ''
	while len(state) < 9:
		num = randrange(9)
		if num not in tiles:
			tiles.append(num)
			if num == 0:
				num = '_'
			state += str(num)
	return state


initial_state = '_13425786'
print('Initial State:')
print_puzzle(initial_state)
problem = Puzzle(initial_state)

node = a_star_search(problem, misplaced_tiles_heuristic)
if node is not None:
	solution = node.solution()
	print("Solution:", "".join(solution))
else:
	print("No solution found")
