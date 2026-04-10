# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False


        skip2 = head
        skip1 = head

        skip1 = skip1.next
            
        if skip2.next:
            skip2 = skip2.next.next
            
        else:
            return False

        while skip1 and skip2:
            if skip1 == skip2:
                return True
            
            skip1 = skip1.next
            
            if skip2.next:
                skip2 = skip2.next.next
            
            else:
                return False
        
        return False
        