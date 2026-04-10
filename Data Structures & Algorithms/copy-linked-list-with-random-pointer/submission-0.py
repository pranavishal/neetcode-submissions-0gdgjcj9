"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        originalHead = head
        newListMap = {}
        while head:
            newListMap[head] = Node(head.val)
            head = head.next
        
        head = originalHead
        
        while head:
            if head.next:
                newListMap[head].next = newListMap[head.next]
            if head.random:
                newListMap[head].random = newListMap[head.random]
            head = head.next
        
        return newListMap[originalHead]

        