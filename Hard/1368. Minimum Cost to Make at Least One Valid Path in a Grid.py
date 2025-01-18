from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        minChanges = [[10 ** 9 for _ in range(numCols)] for j in range(numRows)]
        minChanges[0][0] = 0
        while True:
            prevState = minChanges.copy()
            for row in range(numRows):
                for col in range(numCols):
                    if row > 0:
                        minChanges[row][col] = (
                            min(minChanges[row][col], minChanges[row - 1][col] + (0 if grid[row - 1][col] == 3 else 1)))
                    if col > 0:
                        minChanges[row][col] = (
                            min(minChanges[row][col], minChanges[row][col - 1] + (0 if grid[row][col - 1] == 1 else 1)))
            for row in range(numRows - 1, -1, -1):
                for col in range(numCols - 1, -1, -1):
                    if row < numRows - 1:
                        minChanges[row][col] = (
                            min(minChanges[row][col], minChanges[row + 1][col] + (0 if grid[row + 1][col] == 4 else 1)))
                    if col < numCols - 1:
                        minChanges[row][col] = (
                            min(minChanges[row][col], minChanges[row][col + 1] + (0 if grid[row][col + 1] == 2 else 1)))
            if minChanges == prevState:
                break
        return minChanges[numRows - 1][numCols - 1]
