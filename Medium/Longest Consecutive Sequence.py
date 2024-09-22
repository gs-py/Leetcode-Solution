from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Initialize parent and size dictionaries
        parent = {}
        size = {}

        # Find function with path compression
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # Path compression
                x = parent[x]
            return parent[x]

        # Union function by size
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA != rootB:
                # Union by size
                if size[rootA] > size[rootB]:
                    parent[rootB] = rootA
                    size[rootA] += size[rootB]  # Update size correctly
                else:
                    parent[rootA] = rootB
                    size[rootB] += size[rootA]  # Update size correctly

        # Add element to the union-find structure
        def add(x):
            if x not in parent:
                parent[x] = x  # Set parent to itself (initial root)
                size[x] = 1    # Set size of the component to 1

        # Get the size of the set containing element 'a'
        def getSize(a):
            root = find(a)
            return size[root]

        # Edge case: if no numbers, return 0
        if not nums:
            return 0

        # Add each number to the union-find structure
        for num in nums:
            add(num)
        
        # Union consecutive numbers
        for num in nums:
            if num - 1 in parent:
                union(num, num - 1)
            if num + 1 in parent:
                union(num, num + 1)

        # Find the largest connected component (longest consecutive sequence)
        return max(getSize(num) for num in nums)

# Example usage:
