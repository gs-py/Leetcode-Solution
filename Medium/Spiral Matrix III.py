from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        steps = 1  # initial steps in one direction
        
        r, c = rStart, cStart  # starting position
        direction_index = 0  # start by moving right
        
        while len(result) < rows * cols:
            for _ in range(2):  # there are two movements per direction step count
                for _ in range(steps):
                    # Check if the current position is within bounds
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                    
                    # Move in the current direction
                    r += directions[direction_index][0]
                    c += directions[direction_index][1]
                
                # Change direction (move to the next direction in clockwise)
                direction_index = (direction_index + 1) % 4
            
            # Increase the number of steps after completing a full turn
            steps += 1
        
        return result
