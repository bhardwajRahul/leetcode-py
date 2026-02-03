import pytest

from leetcode_py import logged_test

from .helpers import assert_is_subsequence, run_is_subsequence
from .solution import Solution


class TestTestIsSubsequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, t, expected",
        [
            ("abc", "ahbgdc", True),
            ("axc", "ahbgdc", False),
            ("", "ahbgdc", True),
            ("abc", "", False),
            ("a", "a", True),
            ("a", "b", False),
            ("abc", "abc", True),
            ("abc", "def", False),
            ("ab", "baab", True),
            ("leeeeetcode", "leetcode", False),
            ("aaaaa", "bbaaaabbaab", True),
            ("xyz", "xaybz", True),
            ("abcde", "abxde", False),
        ],
    )
    def test_is_subsequence(self, s: str, t: str, expected: bool):
        result = run_is_subsequence(Solution, s, t)
        assert_is_subsequence(result, expected)
