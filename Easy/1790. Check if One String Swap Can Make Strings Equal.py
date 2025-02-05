class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c = -1
        flag = 0

        for i in range(len(s1)):
            if s1[i] != s2[i] and c == -1:
                c = i
                flag += 1
            elif s1[i] != s2[i]:
                if s1[i] != s2[c] or s2[i] != s1[c]:
                    return False
                flag += 1

        return False if (flag > 2 or flag == 1) else True
