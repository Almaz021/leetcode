from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dop = ListNode(0, head)
        cur = dop
        for i in range(n):
            head = head.next
        while head:
            head = head.next
            cur = cur.next
        cur.next = cur.next.next
        return dop.next
