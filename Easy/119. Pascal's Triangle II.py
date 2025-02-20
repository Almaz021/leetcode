class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []

        size = 0
        while len(ans) != rowIndex + 1:
            cur = [1] * (size + 1)
            if size < 2:
                ans.append(cur)
                size += 1
                continue
            l, r = 0, 1
            for i in range(1, size):
                cur[i] = ans[size-1][l] + ans[size-1][r]
                l += 1
                r += 1
            ans.append(cur)
            size += 1
        return ans[-1]
