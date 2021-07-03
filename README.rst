Let's learn AI - Source Code
============================

Companion to the YouTube series "Let's learn AI" - https://www.youtube.com/channel/UCQFtF8uYQuzmOpzrmKnX77Q  

Search Problem
--------------

Contains the informed and uninformed graph search algorithms.
Must implement a ``Problem`` class: ``from search_problems import Problem``
See ``search.py`` for an example.

Available functions from ``search_problems``:

.. code-block:: python

	def depth_first_search(problem: Problem) -> Optional[Node]: ...
	def depth_first_search_with_reached(problem: Problem) -> Optional[Node]: ...
	def depth_first_search_with_reached_and_tag(problem: Problem) -> Optional[Node]: ...

	def breadth_first_search(problem: Problem) -> Optional[Node]: ...
	def breadth_first_search_with_reached(problem: Problem) -> Optional[Node]: ...
	def breadth_first_search_with_reached_and_tag(problem: Problem) -> Optional[Node]: ...

	def depth_limited_search(problem: Problem, depth: int) -> Optional[Node]: ...
	def iterative_deepening_search(problem: Problem) -> Optional[Node]: ...

