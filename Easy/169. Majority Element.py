from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = {}
        l = len(nums) / 2
        ans = -1
        for i in nums:
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1
            if s[i] > l:
                ans = i
        return ans
