from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = str(l1.val)
        while l1.next is not None:
            l1 = l1.next
            str1 += str(l1.val)
        str2 = str(l2.val)
        while l2.next is not None:
            l2 = l2.next
            str2 += str(l2.val)
        str3 = str(eval(str1 + " + " + str2))[::-1]
        l3 = ListNode()
        head = l3
        for i in str3:
            cur = ListNode(int(i))
            head.next = cur
            head = head.next

        return l3
