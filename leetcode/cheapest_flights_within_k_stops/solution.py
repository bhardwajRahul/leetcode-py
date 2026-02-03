from collections import deque


class Solution:
    # Time: O(K * E) where E is number of flights
    # Space: O(V) where V is number of cities
    def find_cheapest_price(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for from_i, to_i, price_i in flights:
            adj[from_i].append((to_i, price_i))

        # BFS with stops constraint
        prices = [float("inf")] * n
        prices[src] = 0
        queue = deque([(src, 0, 0)])  # (node, current_price, stops)

        while queue:
            node, current_price, stops = queue.popleft()
            if stops > k:
                continue
            for neighbor, price in adj[node]:
                new_price = current_price + price
                if new_price < prices[neighbor]:
                    prices[neighbor] = new_price
                    queue.append((neighbor, new_price, stops + 1))

        return int(prices[dst]) if prices[dst] != float("inf") else -1
