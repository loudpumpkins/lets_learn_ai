
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

	def __rept__(self):
		if self.parent is None:
			return f"<Node '{self.state}' (root node)>"
		return f"<Node '{self.state}' (parent '{self.parent.state}')>"

