from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count_islands(grid):
            visited = [[False] * len(grid[0]) for _ in range(len(grid))]
            def dfs(i, j):
                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or visited[i][j] or grid[i][j] == 0:
                    return
                visited[i][j] = True
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
            
            island_count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and not visited[i][j]:
                        island_count += 1
                        dfs(i, j)
            return island_count
        
        # Step 1: Check the initial number of islands
        initial_islands = count_islands(grid)
        if initial_islands != 1:
            return 0  # Already disconnected or empty
        
        # Step 2: Try changing each land cell (1) into water (0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # Temporarily turn this land cell into water
                    grid[i][j] = 0
                    # Recount the islands
                    if count_islands(grid) != 1:
                        return 1
                    # Revert the change
                    grid[i][j] = 1
        
        # Step 3: If we can't disconnect with one move, return 2
        return 2
