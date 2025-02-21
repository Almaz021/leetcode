class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "abcdefghijklmnopqrstuvwxyz"
        res = ''
        for i in s:
            if i.lower() in a:
                res += i.lower()

        return res == res[::-1]
