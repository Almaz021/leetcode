from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        st = head
        cur = head.next
        d = st
        for i in range(size):
            print(d.val, end=" ")
            d = d.next
        for i in range(size // 2 - 1):
            head.next = cur.next
            cur.next = st
            st = cur
            cur = head.next
        if size % 2 != 0:
            cur = cur.next
        for i in range(size // 2):
            if cur and st:
                if cur.val == st.val:
                    cur = cur.next
                    st = st.next
                else:
                    return False
        return True
