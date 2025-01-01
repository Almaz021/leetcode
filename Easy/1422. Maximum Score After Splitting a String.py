class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            res = max(res, s.count('0', 0, i) + s.count('1', i, len(s)))
        return res
