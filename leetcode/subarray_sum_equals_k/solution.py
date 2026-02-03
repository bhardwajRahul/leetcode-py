from collections import defaultdict


class Solution:
    # Time: O(n)
    # Space: O(n)
    def subarray_sum(self, nums: list[int], k: int) -> int:
        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] = 1
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            if current_sum - k in prefix_sum_counts:
                count += prefix_sum_counts[current_sum - k]
            prefix_sum_counts[current_sum] += 1

        return count
