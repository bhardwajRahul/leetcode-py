import pytest

from leetcode_py import logged_test

from .helpers import assert_is_bipartite, run_is_bipartite
from .solution import Solution


class TestTestIsGraphBipartite:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "graph, expected",
        [
            ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
            ([[1, 3], [0, 2], [1, 3], [0, 2]], True),
            ([[], [2], [1]], True),
            ([[1], [0]], True),
            ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
            ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2, 4], [3]], False),
            ([[1], [0, 2], [1]], True),
            ([[1, 3], [0, 2], [1, 3, 4], [0, 2], [2]], True),
            ([[1, 2], [0, 2], [0, 1]], False),
            ([[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]], False),
            ([[]], True),
            ([[1], [0]], True),
            ([[1, 2, 3], [0, 2], [0, 1, 3, 4], [0, 2], [2]], False),
            ([[1, 3], [0, 2], [1, 3], [0, 2]], True),
        ],
    )
    def test_is_bipartite(self, graph: list[list[int]], expected: bool):
        result = run_is_bipartite(Solution, graph)
        assert_is_bipartite(result, expected)
