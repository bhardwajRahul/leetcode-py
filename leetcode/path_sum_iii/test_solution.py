import pytest

from leetcode_py import logged_test

from .helpers import assert_path_sum, run_path_sum
from .solution import Solution


class TestTestPathSumIii:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, target_sum, expected",
        [
            ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
            ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, 3),
            ([], 1, 0),
            ([1], 1, 1),
            ([1], 0, 0),
            ([1, 2], 3, 1),
            ([1, 2, 3], 3, 2),
            ([1, 2, 3], 5, 0),
            ([1, -2, 3], 1, 1),
            ([1, -2, 3], 2, 0),
            ([1, -2, -3], -3, 1),
            ([0, 1, 1], 1, 4),
            ([1, 0, 1, 0, 1], 1, 6),
            ([0], 0, 1),
            ([-3, -2, 1, 1, 1], -1, 2),
        ],
    )
    def test_path_sum(self, root_list: list[int | None], target_sum: int, expected: int):
        result = run_path_sum(Solution, root_list, target_sum)
        assert_path_sum(result, expected)
