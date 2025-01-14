from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c = []

        a1 = set()
        a2 = set()
        for i in range(len(A)):
            a1.add(A[i])
            a2.add(B[i])
            c.append(len(a1.intersection(a2)))

        return c
