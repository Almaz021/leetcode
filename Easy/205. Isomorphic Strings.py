class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        res = dict()
        a = set()
        for i in range(len(s)):
            if s[i] not in res:
                if t[i] not in a:
                    res[s[i]] = t[i]
                    a.add(t[i])
                else:
                    return False
            elif res[s[i]] != t[i]:
                return False
        return True
