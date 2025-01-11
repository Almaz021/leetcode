class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        a = [0] * 26

        for i in s:
            a[ord(i) - ord('a')] += 1
        count = 0
        for i in a:
            if i % 2 != 0:
                count += 1
        if count > k or len(s) < k:
            return False
        else:
            return True
