from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        d = deque()

        for i in s:
            if i in '({[':
                d.append(i)
            elif len(d) == 0:
                return False
            elif i == ')' and d.pop() != '(':
                return False
            elif i == '}' and d.pop() != '{':
                return False
            elif i == ']' and d.pop() != '[':
                return False
        if len(d) == 0:
            return True
        return False
