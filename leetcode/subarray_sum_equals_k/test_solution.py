import pytest

from leetcode_py import logged_test

from .helpers import assert_subarray_sum, run_subarray_sum
from .solution import Solution


class TestTestSubarraySumEqualsK:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 1, 1], 2, 2),
            ([1, 2, 3], 3, 2),
            ([1], 1, 1),
            ([1], 0, 0),
            ([1, -1, 0], 0, 3),
            ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
            ([1, 2, 3, 4, 5], 5, 2),
            ([1, 1, 1, 1, 1], 2, 4),
            ([1, 2, 1, 2, 1], 3, 4),
            ([-1, -1, 1], 0, 1),
            ([0, 0, 0], 0, 6),
            ([1], 2, 0),
            ([100, 1, 2, 3, 4], 6, 1),
            ([1, 2, 3, 4, 5, 6], 7, 1),
            ([1, -1, 1, -1, 1], 0, 6),
        ],
    )
    def test_subarray_sum(self, nums: list[int], k: int, expected: int):
        result = run_subarray_sum(Solution, nums, k)
        assert_subarray_sum(result, expected)
