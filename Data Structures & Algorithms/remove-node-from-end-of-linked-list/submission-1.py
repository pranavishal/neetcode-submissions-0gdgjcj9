# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeNumberMap = {}
        originalHead = head

        counter = 1
        while head:
            nodeNumberMap[counter] = head
            counter += 1
            head = head.next
        
        listLength = len(list(nodeNumberMap))
        head = originalHead

        if listLength - n not in nodeNumberMap:
            head = head.next
        
        elif listLength - n + 2 not in nodeNumberMap:
            nodeNumberMap[listLength - n].next = None
        
        else:
            nodeNumberMap[listLength - n].next = nodeNumberMap[listLength - n + 2]
        
        return head

            

        
        