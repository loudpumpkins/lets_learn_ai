from typing import Any, Callable, List, NoReturn, Union as U, Tuple, Optional

from search_problems.best_first import best_first_search
from search_problems.util import Node
from search_problems.util import Problem


def greedy_first_search(problem: Problem, h: Callable) -> Optional[Node]:
	"""
	Performs a greedy first search where the evaluation function is:
		f(n) = h(n)

	The best-first search algorithm used does not update nodes in the frontier
	in the event that a better path to an explored node is found. If duplicate
	nodes in the frontier is an issue, change the best-first search algorithm
	to updates nodes in the frontier instead of just adding better nodes to the
	frontier.

	:param problem:
	:param h: Callable heuristic function which takes one argument; Node
	:return: Node or None
	"""
	return best_first_search(problem, h)
