class Solution:
    def minimumLength(self, s: str) -> int:
        a = [0] * 26

        for i in s:
            a[ord(i) - ord('a')] += 1

        ans = 0
        for i in a:
            if i == 0:
                continue
            if i == 1 or i == 2:
                ans += i
            elif i % 2 != 0:
                ans += 1
            else:
                ans += 2

        return ans
