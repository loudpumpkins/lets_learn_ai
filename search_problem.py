from search_problems import Problem, iterative_deepening_search


class CGW(Problem):
	"""
	This class implements a Cabbage-Goat-Wolf problem as a sub-class of the
	search `Problem` class.

	The values of the state member variables of instances of this class are
	represented in a tuple as follows:

	(human, left, right)

	Where:
	human is an integer;
	  1 = human (and boat) on left side,
	  2 = human (and boat) on right side,

	left is a string containing zero to three of the characters "CGW" indicating
	which entities are on the left side of the river;

	right is a string containing zero to three of the characters "CGW"
	indicating which entities are on the right side of the river.

	The initial state of the CGW problem is (1,"CGW","").
	"""
	count = 0
	visited = set()

	def __init__(self, initial_state):
		"""
		Initialize a CGW state member variables based on the passed arguments.
		"""
		super().__init__(self.validate(initial_state))

	def actions(self, state):
		"""
		Return a list of valid actions to take. Which are simply the animal that
		needs to be moved to the other side with the human.

		Recall that a state is: (human, left_side, right_side) where human is
		1 if on the left side or 2 if on the right.

		So we can access the side we are working on using:

			state[state[0]] -> state[human location] -> the side human is on

		"""
		actions = []
		for animal in state[state[0]]:
			actions.append(animal)  # animal crossing with human
		actions.append(None)  # the human crossing alone

		return actions

	def is_goal(self, state):
		"""
	    Return True if the problem is solved.  I.e.: human and all items are on
	    the right side.
	    """
		if state in CGW.visited:
			print('ALREADY VISITED', state)
		CGW.visited.add(state)
		print(CGW.count, '-', state)
		CGW.count = CGW.count + 1
		return state[0] == 2 and state[2] == "CGW"

	def transition(self, state, action):
		"""
		The transition is to always move the human from one side to the other.
		The action contains a letter "C", "G", "W" to indicate which animal
		should the human take with him, or `None` if the human is to move alone.
		"""
		animal = action
		human = state[0]
		left_side = state[1]
		right_side = state[2]

		if human == 1:
			# human is going from left to right, move animal from left to right
			human = 2
			left_side = self._remove_animal(left_side, animal)
			right_side = self._add_animal(right_side, animal)

		elif human == 2:
			human = 1
			# human is going from right to left, move animal from right to left
			right_side = self._remove_animal(right_side, animal)
			left_side = self._add_animal(left_side, animal)

		else:  # Where is the human ?
			raise IndexError("State[0] 'human' must be '1' or '2'.")

		state = (human, left_side, right_side)
		return self.validate(state)

	def validate(self, state):
		"""
		Update a state variable based on the goat eating the cabbage or the wolf
		eating the goat.
		"""
		if state[0] == 1:  # human is on left side
			right = state[2]  # retrieve the contents of the right side
			if "G" in right:  # goat is on right side
				right = self._remove_animal(right, "C")  # goat eats cabbage
			if "W" in right:  # wolf is on right side
				right = self._remove_animal(right, "G")  # wolf eats cabbage
			# reconstruct state which with new right-side contents
			state = (state[0], state[1], right)

		elif state[0] == 2:  # human is on right side
			left = state[1]  # retrieve the contents of the left side
			if "G" in left:  # goat is on the left side
				left = self._remove_animal(left, "C")  # goat eats cabbage
			if "W" in left:  # wolf is on the left side
				left = self._remove_animal(left, "G")  # wolf eats goat
			# reconstruct state with new left-side contents
			state = (state[0], left, state[2])

		else:  # Where is the human ?
			raise IndexError("State[0] 'human' must be '1' or '2'.")
		return state

	def _remove_animal(self, input_string, animal):
		"""
		This is a utility function that returns a string that matches the
		input_string except with the given animal (letter) removed.

		exp: input: "CGW", animal: "G", output: "CW"
		"""
		if animal is None:
			return input_string
		return input_string.replace(animal, "")

	def _add_animal(self, input_string, animal):
		"""
		This is a utility function that returns a string that matches the
		input_string with the given animal added in alphabetical position.
		"""
		if animal is None:
			return input_string
		return "".join(sorted(input_string + animal))


initial_state = (1, "CGW", "")
node = iterative_deepening_search(CGW(initial_state))
if node is not None:
	solution = node.solution()
	for index, action in enumerate(solution):
		if action is None:
			solution[index] = '-'
	print("".join(solution))
else:
	print("No solution found")
