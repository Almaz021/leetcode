class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1, p2 = 0, len(needle)
        for i in range(p2, len(haystack) + 1):
            if haystack[p1:p2] == needle:
                return p1
            p1 += 1
            p2 += 1
        return -1
