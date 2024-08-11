from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(a, b, c, d, e, f, g, h, i):
            # Check if all elements are distinct and between 1 to 9
            if sorted([a, b, c, d, e, f, g, h, i]) != list(range(1, 10)):
                return False
            # Check if the rows, columns, and diagonals sum to 15
            return (a + b + c == 15 and
                    d + e + f == 15 and
                    g + h + i == 15 and
                    a + d + g == 15 and
                    b + e + h == 15 and
                    c + f + i == 15 and
                    a + e + i == 15 and
                    c + e + g == 15)
        
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        # Iterate through each 3x3 subgrid
        for r in range(rows - 2):
            for c in range(cols - 2):
                if grid[r + 1][c + 1] != 5:
                    continue  # Central cell must be 5 for it to be a magic square
                if isMagic(grid[r][c], grid[r][c+1], grid[r][c+2],
                           grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                           grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    count += 1
        
        return count
