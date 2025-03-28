from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 0
        for i in range(1, len(nums)):
            if nums[ind] != nums[i]:
                ind += 1
                nums[ind] = nums[i]
        return ind + 1
