from typing import Any, Callable, List, NoReturn, Union as U, Tuple, Optional

from search_problems.best_first import best_first_search
from search_problems.util import Node
from search_problems.util import Problem


def a_star_search(problem: Problem, h: Callable) -> Optional[Node]:
	"""
	Performs a best-first search where the evaluation function is:
		f(n) = g(n) + h(n)

	The best-first search algorithm used does not update nodes in the frontier
	in the event that a better path to an explored node is found. To avoid
	having duplicate nodes in the frontier, either use a monotonic heuristic
	or change the best-first search algorithm to updates nodes in the frontier.

	:param problem:
	:param h: Callable heuristic function which takes one argument; Node
	:return: Node or None
	"""
	return best_first_search(problem, lambda node: node.path_cost + h(node))
