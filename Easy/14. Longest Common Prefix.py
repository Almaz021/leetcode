from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = strs[0]
        res = len(a)
        for i in range(1, len(strs)):
            ind = 0
            for j in range(min(len(a), len(strs[i]))):
                if strs[i][j] == a[j]:
                    ind += 1
                else:
                    res = min(res, ind)
        return a[:res]
