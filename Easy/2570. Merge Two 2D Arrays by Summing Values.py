from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        a = {}
        for i in nums1:
            a[i[0]] = i[1]
        for i in nums2:
            if i[0] not in a:
                a[i[0]] = i[1]
            else:
                a[i[0]] += i[1]
        res = []
        for i in sorted(a.keys()):
            res.append([i, a[i]])

        return res
