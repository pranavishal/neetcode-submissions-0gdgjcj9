# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2

        firstNode = None

        if curr1 is None:
            if curr2 is None:
                return None
            
            firstNode = ListNode(curr2.val, None)
            curr2 = curr2.next
        
        else:
            if curr2 is None:
                firstNode = ListNode(curr1.val, None)
                curr1 = curr1.next
            
            else:
                if curr1.val < curr2.val:
                    firstNode = ListNode(curr1.val, None)
                    curr1 = curr1.next
                
                else:
                    firstNode = ListNode(curr2.val, None)
                    curr2 = curr2.next
        
        prevNode = firstNode
        while True:
            currNode = ListNode(-1, None)
            if curr1 is None and curr2 is None:
                break
            
            if curr1 is None:
                if curr2 is None:
                    return None
            
                currNode.val = curr2.val
                prevNode.next = currNode
                prevNode = prevNode.next
                curr2 = curr2.next
        
            else:
                if curr2 is None:
                    currNode.val = curr1.val
                    prevNode.next = currNode
                    prevNode = prevNode.next
                    curr1 = curr1.next
            
                else:
                    if curr1.val < curr2.val:
                        currNode.val = curr1.val
                        prevNode.next = currNode
                        prevNode = prevNode.next
                        curr1 = curr1.next
                
                    else:
                        currNode.val = curr2.val
                        prevNode.next = currNode
                        prevNode = prevNode.next
                        curr2 = curr2.next
            

        

    
                
        return firstNode
        