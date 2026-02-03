from collections import deque


class Solution:
    # Time: O(n)
    # Space: O(k)
    def max_sliding_window(self, nums: list[int], k: int) -> list[int]:
        result: list[int] = []
        # Store indices of elements in decreasing order of values
        dq: deque[int] = deque()

        for i, num in enumerate(nums):
            # Remove indices that are out of the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove indices whose corresponding values are less than the current value
            while dq and nums[dq[-1]] < num:
                dq.pop()

            # Add current index
            dq.append(i)

            # Add maximum to result when we have a complete window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
