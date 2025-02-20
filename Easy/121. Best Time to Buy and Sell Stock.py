from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        ma = prices[0]

        prof = 0

        for i in prices[1:]:
            if i > ma:
                ma = i
                prof = max(prof, ma - mi)
            elif i < mi:
                mi = i
                ma = i

        return prof
