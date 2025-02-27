from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)

        for i in range(len(boxes)):
            if boxes[i] == '1':
                for j in range(len(boxes)):
                    ans[j] += abs(i - j)
        return ans
