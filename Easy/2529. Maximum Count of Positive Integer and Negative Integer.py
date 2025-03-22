class Solution:
    def maximumCount(self, nums):
        p = 0
        n = 0

        for num in nums:
            if num > 0:
                p += 1
            elif num < 0:
                n += 1

        return max(p, n)
