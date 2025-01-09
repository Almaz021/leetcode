from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        deq = deque()
        ma = 0
        for ch in s:
            if ch in se:
                while ch in se:
                    se.remove(deq.popleft())
            se.add(ch)
            deq.append(ch)
            ma = max(ma, len(deq))

        return max(ma, len(deq))
