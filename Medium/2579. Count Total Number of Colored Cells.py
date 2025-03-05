class Solution:
    def coloredCells(self, n: int) -> int:
        s = 1
        if n == 1:
            return s
        for i in range(1, n):
            s += 4*i
        return s
