from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        st = head
        cur = head.next
        while cur:
            head.next = cur.next
            cur.next = st
            st = cur
            cur = head.next
        return st
