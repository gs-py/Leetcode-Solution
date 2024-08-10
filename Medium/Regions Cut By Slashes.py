from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        expanded_grid = [[0] * n * 3 for _ in range(n * 3)]
        
        # Expand the grid
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    expanded_grid[i * 3][j * 3 + 2] = 1
                    expanded_grid[i * 3 + 1][j * 3 + 1] = 1
                    expanded_grid[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == '\\':
                    expanded_grid[i * 3][j * 3] = 1
                    expanded_grid[i * 3 + 1][j * 3 + 1] = 1
                    expanded_grid[i * 3 + 2][j * 3 + 2] = 1
        
        # Function to perform DFS
        def dfs(x, y):
            if 0 <= x < 3 * n and 0 <= y < 3 * n and expanded_grid[x][y] == 0:
                expanded_grid[x][y] = 1
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
        
        regions = 0
        for i in range(3 * n):
            for j in range(3 * n):
                if expanded_grid[i][j] == 0:
                    dfs(i, j)
                    regions += 1
        
        return regions
