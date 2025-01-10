from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        a = [0] * 26
        ans = []

        for i in words2:
            b = [0] * 26
            for j in i:
                b[ord(j) - ord('a')] += 1
                if b[ord(j) - ord('a')] > a[ord(j) - ord('a')]:
                    a[ord(j) - ord('a')] = b[ord(j) - ord('a')]

        for i in words1:
            flag = True
            l = [0] * 26
            for j in i:
                l[ord(j) - ord('a')] += 1

            for k in range(26):
                if l[k] < a[k]:
                    flag = False
                    break

            if flag:
                ans.append(i)

        return ans
