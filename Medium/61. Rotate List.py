from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        k = k % size
        if k == 0:
            return head
        p1 = head
        p2 = head
        for i in range(k):
            p2 = p2.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        new_head = p1.next
        p2.next = head
        p1.next = None

        return new_head
