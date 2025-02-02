from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = False
        l = len(nums)

        for i in range(l):
            if nums[i] > nums[(i + 1) % l] and not flag:
                flag =  True
            elif nums[i] > nums[(i + 1) % l]:
                return False
        return True
