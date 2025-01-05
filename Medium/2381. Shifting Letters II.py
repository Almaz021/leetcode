from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                shift[start] += 1
                shift[end + 1] -= 1
            else:
                shift[start] -= 1
                shift[end + 1] += 1

        pref = 0
        shifts_array = [0] * n
        for i in range(n):
            pref += shift[i]
            shifts_array[i] = pref

        result = []
        for i in range(n):
            new_char = chr(((ord(s[i]) - ord('a') + shifts_array[i]) % 26) + ord('a'))
            result.append(new_char)

        return ''.join(result)
