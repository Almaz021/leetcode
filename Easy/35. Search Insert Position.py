from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                return mid
            else:
                l = mid + 1

        return l
