from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 % 2 == 0 and l2 % 2 == 0:
            return 0
        nums = []
        for i in nums1:
            if l2 % 2 != 0:
                nums.append(i)
        for i in nums2:
            if l1 % 2 != 0:
                nums.append(i)
        r = nums[0]
        for i in nums[1:]:
            r ^= i
        return r
