class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def find_circle_num(self, is_connected: list[list[int]]) -> int:
        n = len(is_connected)
        visited = [False] * n

        def dfs(city: int) -> None:
            visited[city] = True
            for neighbor in range(n):
                if is_connected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        provinces = 0
        for city in range(n):
            if not visited[city]:
                dfs(city)
                provinces += 1

        return provinces
