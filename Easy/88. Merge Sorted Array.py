from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        s1 = 0
        s2 = 0
        ans = []
        for i in range(n + m):
            if s1 < m and s2 < n:
                if nums1[s1] < nums2[s2]:
                    ans.append(nums1[s1])
                    s1 += 1
                else:
                    ans.append(nums2[s2])
                    s2 += 1
            elif s1 < m:
                ans.append(nums1[s1])
                s1 += 1
            elif s2 < n:
                ans.append(nums2[s2])
                s2 += 1
        for i in range(n + m):
            nums1[i] = ans[i]
        print(nums1)