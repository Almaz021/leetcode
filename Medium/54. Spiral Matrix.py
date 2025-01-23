from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, d, u, r = -1, len(matrix), 0, len(matrix[0])
        s = len(matrix) * len(matrix[0])
        x, y = 0, 0
        di = 1
        ans = []
        size = 0
        while size != s:
            if di == 1:
                if y + 1 < r:
                    ans.append(matrix[x][y])
                    size += 1
                    y += 1
                else:
                    r -= 1
                    di = 2
            elif di == 2:
                if x + 1 < d:
                    ans.append(matrix[x][y])
                    size += 1
                    x += 1
                else:
                    d -= 1
                    di = 3
            elif di == 3:
                if y - 1 > l:
                    ans.append(matrix[x][y])
                    size += 1
                    y -= 1
                else:
                    l += 1
                    di = 4
            elif di == 4:
                if x - 1 > u:
                    ans.append(matrix[x][y])
                    size += 1
                    x -= 1
                else:
                    u += 1
                    di = 1
            if size + 1 == s:
                ans.append(matrix[x][y])
                size += 1
        return ans
