from typing import Any, Callable, List, NoReturn, Union as U, Tuple, Optional
import queue

from search_problems.util import Node
from search_problems.util import Problem


def depth_first_search(problem: Problem) -> Optional[Node]:
	"""
	Takes in an implemented `Problem` and returns a `Node` once a solution is
	found or `None` otherwise.

	The `Node` contains the solution, path costs and all the details of a
	particular solution.

	This algorithm will NOT track reached nodes and may run indefinitely in the
	event that a cycle is present.

	:param problem: Implemented Problem class
	:return: Node or None
	"""
	frontier = queue.LifoQueue()
	frontier.put(Node(problem.initial_state))

	while not frontier.empty():
		node: Node = frontier.get()
		if problem.is_goal(node.state):
			return node
		# map(frontier.put, problem.expand(node))
		for child in problem.expand(node):
			frontier.put(child)
	return None


def depth_first_search_with_reached(problem: Problem) -> Optional[Node]:
	"""
	Takes in an implemented `Problem` and returns a `Node` once a solution is
	found or `None` otherwise.

	The `Node` contains the solution, path costs and all the details of a
	particular solution.

	This algorithm will track previously reached states and will not visit
	them again.

	:param problem: Implemented Problem class
	:return: Node or None
	"""
	frontier = queue.LifoQueue()
	frontier.put(Node(problem.initial_state))

	while not frontier.empty():
		node: Node = frontier.get()
		if problem.is_goal(node.state):
			return node
		for child in problem.expand(node):
			if not child.explored(child.state):
				frontier.put(child)
	return None


def depth_first_search_with_reached_and_tag(problem: Problem) -> Optional[Node]:
	"""
	Takes in an implemented `Problem` and returns a `Node` once a solution is
	found or `None` otherwise.

	The `Node` contains the solution, path costs and all the details of a
	particular solution.

	This algorithm will track previously reached states and will not visit
	them again. It will also test for goal at generation; before it is added to
	the frontier.

	:param problem: Implemented Problem class
	:return: Node or None
	"""
	frontier = queue.LifoQueue()
	frontier.put(Node(problem.initial_state))

	while not frontier.empty():
		node: Node = frontier.get()
		for child in problem.expand(node):
			if not child.explored(child.state):
				if problem.is_goal(child.state):
					return child
				frontier.put(child)
	return None