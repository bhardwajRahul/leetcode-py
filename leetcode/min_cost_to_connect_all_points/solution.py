import heapq


class Solution:
    # Time: O(n^2 * log(n)) for Prim's algorithm
    # Space: O(n)
    def min_cost_connect_points(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        def manhattan_distance(p1: list[int], p2: list[int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        visited = [False] * n
        min_heap: list[tuple[int, int]] = [(0, 0)]  # (cost, node)
        total_cost = 0
        edges_used = 0

        while min_heap and edges_used < n:
            cost, node = heapq.heappop(min_heap)
            if visited[node]:
                continue
            visited[node] = True
            total_cost += cost
            edges_used += 1

            for neighbor in range(n):
                if not visited[neighbor]:
                    distance = manhattan_distance(points[node], points[neighbor])
                    heapq.heappush(min_heap, (distance, neighbor))

        return total_cost
