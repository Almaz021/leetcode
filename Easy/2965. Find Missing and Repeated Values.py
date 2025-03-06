from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        c = set()
        f = set([i for i in range(1, len(grid) ** 2 + 1)])
        a = -1
        b = -1
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] not in c:
                    c.add(grid[i][j])
                else:
                    a = grid[i][j]
        b = f.difference(c).pop()

        return [a, b]
