class Solution:
    def clearDigits(self, s: str) -> str:
        l = 0
        res = list(s)

        for i in range(len(res)):
            if res[i].isdigit():
                l = max(l - 1, 0)
            else:
                res[l] = res[i]
                l += 1

        res = res[:l]

        return "".join(res)
