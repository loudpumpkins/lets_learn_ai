from typing import Any, Callable, List, NoReturn, Union as U, Tuple, Optional
import heapq
import itertools

from search_problems.util import Node
from search_problems.util import Problem


def best_first_search(problem: Problem, f: Callable) -> Optional[Node]:
	"""
	Takes in an implemented `Problem` and returns a `Node` once a solution is
	found or `None` otherwise. Uses a priority queue to always explore nodes
	in the frontier with the lowest f(n) value.

	This algorithm will track reached/explored nodes and will insert a node into
	the frontier if that node has not been reached before, or if the new path has
	a lower cost. To avoid duplicates in the frontier, use an A* search with a
	monotonic heuristic.

	:param problem: Implemented Problem class
	:param f: Callable evaluation function that takes in 1 argument; Node
	:return: Node or None
	"""
	explored = {}
	frontier = []

	root = Node(problem.initial_state)
	counter = itertools.count()  # tie breaker for heapq
	heapq.heappush(frontier, (f(root), next(counter), root))

	while frontier:
		node: Node = heapq.heappop(frontier)[2]
		if problem.is_goal(node.state):
			return node
		for child in problem.expand(node):
			if child.state in explored \
				and f(child) >= explored[child.state].path_cost:
				continue
			heapq.heappush(frontier, (f(child), next(counter), child))
			explored[node.state] = child
	return None
