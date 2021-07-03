from typing import Any, Callable, List, NoReturn, Union as U, Tuple, Optional
import queue
import sys

from search_problems.util import Node
from search_problems.util import Problem


def depth_limited_search(problem: Problem, depth: int) -> Optional[Node]:
	"""
	Performs a depth-first search with a given max depth where the depth value itself
	is NOT included in the search. Meaning that a depth of 1 will traverse the root
	node but NOT it's children. It will stop once depth 1 is reached.

	This algorithm will prevent cycles by asserting a child state has not been
	visited by one of the parent nodes. However, it will not prevent the search
	of redundant paths.

	Returns a `Node` if solution is found or `None` otherwise.

	:param problem: Problem
	:param depth: int
	:return: Node or None
	"""
	frontier = queue.LifoQueue()
	frontier.put(Node(problem.initial_state))

	while not frontier.empty():
		node: Node = frontier.get()
		if problem.is_goal(node.state):
			return node
		for child in problem.expand(node):
			path = child.path_to_root()
			if any(filter(lambda n: n.state == child.state, path)) \
				or len(path) > depth:
				# this node has either been visited or max depth reached - stop
				continue
			if child not in frontier:
				frontier.put(child)
	return None


def iterative_deepening_search(problem: Problem) -> Optional[Node]:
	"""
	Iterative deepening search uses a depth limited search with increasing limits.

	Takes in an implemented `Problem` and returns a `Node` once a solution is
	found or `None` otherwise.

	The `Node` contains the solution, path costs and all the details of a
	particular solution.

	:param problem: Problem
	:return: Node or None
	"""
	for e in range(start=1, stop=sys.maxsize):
		result = depth_limited_search(problem, e)
		if isinstance(result, Node):
			return result
