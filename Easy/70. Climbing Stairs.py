class Solution:
    def climbStairs(self, n: int) -> int:
        a = [0, 1, 2]

        for i in range(n - 2):
            a.append(a[-1] + a[-2])

        return a[n]
