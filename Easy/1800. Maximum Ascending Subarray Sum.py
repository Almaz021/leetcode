from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s = nums[0]
        m = 0
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                s += nums[i + 1]
            else:
                m = max(m, s)
                s = nums[i + 1]

        return max(m, s)
