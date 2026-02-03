import pytest

from leetcode_py import logged_test

from .helpers import assert_single_number, run_single_number
from .solution import Solution


class TestTestSingleNumberIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 1, 3, 2, 5], [3, 5]),
            ([-1, 0], [-1, 0]),
            ([0, 1], [1, 0]),
            ([1, 1, 2, 2, 3, 4], [3, 4]),
            ([5, 5, 6, 6, 7, 8], [7, 8]),
            ([10, 20, 10, 30, 20, 40], [30, 40]),
            ([0, 0, 1, 1, 2, 3], [2, 3]),
            ([-2, -2, -3, -3, -4, -5], [-4, -5]),
            ([100, 100, 101, 102], [101, 102]),
            ([1, 2], [1, 2]),
            ([-1, -1, 0, 1], [0, 1]),
            ([7, 7, 8, 8, 9, 10, 10, 11, 11, 12], [9, 12]),
            ([2**30, 2**30 + 1], [2**30, 2**30 + 1]),
            ([-(2**31), -(2**31) + 1, -(2**31), -(2**31) + 2], [-(2**31) + 1, -(2**31) + 2]),
            ([1, 1, 2, 2, 3, 3, 4, 4, 5, 6], [5, 6]),
        ],
    )
    def test_single_number(self, nums: list[int], expected: list[int]):
        result = run_single_number(Solution, nums)
        assert_single_number(result, expected)
