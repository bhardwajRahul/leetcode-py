class Solution:
    # Time: O(len(t))
    # Space: O(1)
    def is_subsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in t:
            if i < len(s) and char == s[i]:
                i += 1
        return i == len(s)
