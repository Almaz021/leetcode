class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(map(str.strip, s.split()))[::-1])
