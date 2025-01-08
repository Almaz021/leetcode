from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                c = len(words[i])
                if words[i] == words[j][:c] and words[i] == words[j][-c:]:
                    ans += 1
        return ans
