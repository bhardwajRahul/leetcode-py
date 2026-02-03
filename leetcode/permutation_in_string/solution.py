class Solution:
    # Time: O(len(s2))
    # Space: O(1) - only 26 letters
    def check_inclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for c in s1:
            s1_count[ord(c) - ord("a")] += 1

        for i in range(len2):
            window_count[ord(s2[i]) - ord("a")] += 1
            if i >= len1:
                window_count[ord(s2[i - len1]) - ord("a")] -= 1
            if i >= len1 - 1 and window_count == s1_count:
                return True

        return False
