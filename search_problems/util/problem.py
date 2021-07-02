from search_problems.util.node import Node


class Problem(object):
	"""
	An abstract search problem with core functionality that needs to be
	implemented.
	"""

	def __init__(self, initial_state):
		self.initial_state = initial_state

	def actions(self, state):
		"""
		Generate a list of actions that can be taken given any state.

		:param state: Any: Same datatype as the `state` in `Node`
		:return: list
		"""
		raise NotImplemented("Abstract class method not implemented")

	def is_goal(self, state):
		"""
		Test the given state to see if a goal has been reached. The `state` is
		of the same data type as the state in `Node` from `search_problem.util`

		:param state: Any: Same datatype as the `state` in `Node`
		:return: bool
		"""
		raise NotImplemented("Abstract class method not implemented")

	def transition(self, state, action):
		"""
		Generate the resultant state given any state and a valid action.

		:param state: Any: Same datatype as the `state` in `Node`
		:param action: Any
		:return: result_state: Any: Same datatype as the `state` in `Node`
		"""
		raise NotImplemented("Abstract class method not implemented")

	def expand(self, node: Node):
		"""
		Expand the given node with a state, return a list of successor nodes
		using the problem's actions and transitions.

		:param node: Node
		:return: list[Node]
		"""
		return [Node(self.transition(node.state, action)) for action in
		        self.actions(node.state)]
