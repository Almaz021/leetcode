class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        prev = -1
        while l < r:
            mid = (l + r) / 2

            if (mid * mid) > x:
                r = mid
            elif (mid * mid) == x:
                return int(mid)
            else:
                l = mid
            if prev == mid:
                return int(prev)
            prev = mid
        return int(l)
