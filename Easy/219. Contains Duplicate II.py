from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = {}
        for i in range(len(nums)):
            if nums[i] not in s:
                s[nums[i]] = i
            else:
                if abs(s[nums[i]] - i) <= k:
                    return True
                s[nums[i]] = i
        return False
