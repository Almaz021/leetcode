from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        up_sum = sum(grid[0])
        down_sum = 0
        mi = float("inf")
        for i in range(len(grid[0])):
            up_sum -= grid[0][i]
            mi = min(mi, max(up_sum, down_sum))
            down_sum += grid[1][i]
        return mi
