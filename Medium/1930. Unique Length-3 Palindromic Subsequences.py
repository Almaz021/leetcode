class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        count = 0

        for char in first:
            start = first[char]
            end = last[char]
            if end > start + 1:
                unique_middle_chars = set(s[start + 1:end])
                count += len(unique_middle_chars)

        return count
