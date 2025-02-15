from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        s = nums[-k:] + nums[:-k]
        if k != 0:
            nums.clear()
            nums += s
