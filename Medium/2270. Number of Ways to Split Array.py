from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pref = 0
        s = sum(nums)
        ans = 0
        for i in range(0, len(nums) - 1):
            pref += nums[i]
            ans += 1 if s <= 2 * pref else 0
        return ans
