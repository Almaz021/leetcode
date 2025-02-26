from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = {headA}
        while headA:
            headA = headA.next
            s.add(headA)
        while headB:
            if headB in s:
                return headB
            headB = headB.next
        return None

        # if not headA or not headB:
        #     return None
        # pA, pB = headA, headB
        # while pA != pB:
        #     pA = pA.next if pA else headB
        #     pB = pB.next if pB else headA
        # return pA
