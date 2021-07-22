Let's learn AI - Source Code
============================

Companion AI lessons on - https://loudpumpkins.com/

Search Problem
--------------
https://loudpumpkins.com/category/problem-solving-ai/

Contains the informed and uninformed graph search algorithms.
Must implement a ``Problem`` class: ``from search_problems import Problem``

See ``search_problem_uninformed.ipynb`` for detailed explanation or
``search_problem_uninformed.py`` / ``search_problem_uninformed.py`` for
implementation examples.

Available functions from ``search_problems``:

.. code-block:: python

	# uninformed search algorithms
	def depth_first_search(problem: Problem) -> Optional[Node]: ...
	def depth_first_search_with_reached(problem: Problem) -> Optional[Node]: ...
	def depth_first_search_with_reached_and_tag(problem: Problem) -> Optional[Node]: ...

	def breadth_first_search(problem: Problem) -> Optional[Node]: ...
	def breadth_first_search_with_reached(problem: Problem) -> Optional[Node]: ...
	def breadth_first_search_with_reached_and_tag(problem: Problem) -> Optional[Node]: ...

	def depth_limited_search(problem: Problem, depth: int) -> Optional[Node]: ...
	def iterative_deepening_search(problem: Problem) -> Optional[Node]: ...

	# informed search algorithms
	def greedy_first_search(problem: Problem, h: Callable) -> Optional[Node]: ...
	def a_star_search(problem: Problem, h: Callable) -> Optional[Node]: ...
	def best_first_search(problem: Problem, f: Callable) -> Optional[Node]: ...

