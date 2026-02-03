from collections import defaultdict

from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def path_sum(self, root: TreeNode[int] | None, target_sum: int) -> int:
        """Count paths where sum equals target_sum using prefix sum technique."""
        self.count = 0
        prefix_counts: defaultdict[int, int] = defaultdict(int)
        prefix_counts[0] = 1  # Empty path prefix

        def dfs(node: TreeNode[int] | None, current_sum: int) -> None:
            if not node:
                return

            current_sum += node.val
            # Check if (current_sum - target_sum) exists in prefix_counts
            self.count += prefix_counts[current_sum - target_sum]
            # Add current sum to prefix_counts
            prefix_counts[current_sum] += 1

            # Recurse on children
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # Backtrack: remove current sum from prefix_counts
            prefix_counts[current_sum] -= 1

        dfs(root, 0)
        return self.count
