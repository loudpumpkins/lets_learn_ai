
class Node(object):
	"""
	A single node in a search tree.

	Members:
		state - The state to which the node corresponds.
		parent - The node in the tree that generated this node. `None` for root
			nodes.
		action - the action that was applied to the parent's state to generate
			this node. `None for root nodes.
		path_cost - The total cost of the path from the initial state to this
			node. Denoted as g(n). `0` for root nodes
	"""

	def __init__(self, state, parent=None, action=None, path_cost=0):
		self.state = state
		self.parent = parent
		self.action = action
		self.path_cost = path_cost

	def __repr__(self):
		if self.parent is None:
			return f"<Node '{self.state}' (root node)>"
		return f"<Node '{self.state}' (parent '{self.parent.state}')>"

	def explored(self, state):
		"""
		Check to see if the given state is the state of one of the parent nodes.
		:param state: type(self.state)
		:return: bool
		"""
		if any(filter(lambda n: n.state == state, self.path_to_root())):
			return True
		return False

	def path_to_root(self):
		"""
		Returns a list of all nodes from the current node to the root node (inclusive)
		:return: List[Node]
		"""
		path = []
		node = self
		while node is not None:
			path.append(node)
			node = node.parent
		return path
