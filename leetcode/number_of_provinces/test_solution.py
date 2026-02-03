import pytest

from leetcode_py import logged_test

from .helpers import assert_find_circle_num, run_find_circle_num
from .solution import Solution


class TestTestNumberOfProvinces:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "is_connected, expected",
        [
            ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
            ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
            ([[1]], 1),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1),
            ([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 2),
            ([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]], 2),
            ([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]], 2),
            ([[1, 1, 0], [1, 1, 1], [0, 1, 1]], 1),
            ([[1, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]], 1),
            ([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 4),
            ([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 3),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1),
            ([[1, 0], [0, 1]], 2),
        ],
    )
    def test_find_circle_num(self, is_connected: list[list[int]], expected: int):
        result = run_find_circle_num(Solution, is_connected)
        assert_find_circle_num(result, expected)
