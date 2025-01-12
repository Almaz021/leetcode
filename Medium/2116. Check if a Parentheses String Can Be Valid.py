class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        c = 0
        free = 0

        for i in range(len(s)):
            if locked[i] == '0':
                free += 1
            elif s[i] == '(':
                c += 1
            else:
                if c > 0:
                    c -= 1
                elif free > 0:
                    free -= 1
                else:
                    return False

        c = 0
        free = 0

        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':
                free += 1
            elif s[i] == ')':
                c += 1
            else:
                if c > 0:
                    c -= 1
                elif free > 0:
                    free -= 1
                else:
                    return False

        return True
