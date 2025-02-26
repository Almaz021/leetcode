class Solution:
    def isHappy(self, n: int) -> bool:
        s = {n}
        r = 0
        while n != 1:
            r = 0
            for i in str(n):
                r += int(i) ** 2
            if r in s:
                return False
            else:
                n = r
                s.add(n)
        return True
