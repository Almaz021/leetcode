from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        s = 0
        p1 = 0
        for i in range(len(nums)):
            s += nums[i]
            while s >= target and p1 < len(nums):
                res = min(res, i - p1 + 1)
                s -= nums[p1]
                p1 += 1
        return res if res != len(nums) + 1 else 0
