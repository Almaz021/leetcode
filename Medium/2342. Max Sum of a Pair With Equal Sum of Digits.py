from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        s = {}
        ans = -1
        for i in nums:
            su = sum(int(j) for j in str(i))
            if su not in s:
                s[su] = [i]
            else:
                l = s[su]
                if len(l) == 1:
                    l.append(i)
                    l.sort()
                else:
                    if l[-1] < i:
                        l[-2], l[-1] = l[-1], i
                    elif l[-2] < i:
                        l[-2] = i
                s[su] = l

        for i in s.values():
            if len(i) == 2:
                ans = max(ans, i[0] + i[1])

        return ans
