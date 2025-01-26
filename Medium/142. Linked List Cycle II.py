from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        while slow:
            if slow.val == 10 ** 6:
                return slow
            slow.val = 10 ** 6
            slow = slow.next
        return None
