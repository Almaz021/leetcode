from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        s = {}
        new_head = None
        cur = head
        while cur:
            if not new_head:
                new_head = Node(x=cur.val)
                s[cur] = new_head
            else:
                s[cur] = Node(x=cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                s[cur].next = s[cur.next]
            if cur.random:
                s[cur].random = s[cur.random]
            cur = cur.next
        return new_head
