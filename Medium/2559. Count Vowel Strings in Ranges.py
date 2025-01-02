from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pref = [0] * len(words)
        vowels = 'aeiou'
        pref[0] = 1 if words[0][0] in vowels and words[0][-1] in vowels else 0
        for i in range(1, len(words)):
            s = 1 if words[i][0] in vowels and words[i][-1] in vowels else 0
            pref[i] = pref[i - 1] + s
        ans = []
        for i in queries:
            if i[0] == 0:
                ans.append(pref[i[1]])
            else:
                ans.append(pref[i[1]] - pref[i[0] - 1])
        return ans
