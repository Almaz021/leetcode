from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        mapping = {mat[i][j]: (i, j) for i in range(rows) for j in range(cols)}

        row_counts = [0] * rows
        col_counts = [0] * cols

        for ind, value in enumerate(arr):
            if value in mapping:
                r, c = mapping[value]
                row_counts[r] += 1
                col_counts[c] += 1

                if row_counts[r] == cols or col_counts[c] == rows:
                    return ind
