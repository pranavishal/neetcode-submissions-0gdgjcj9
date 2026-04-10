# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        nxt = dummy

        while True:
            min_val = float('inf')
            for i in range(len(lists)):
                if lists[i] == None:
                    continue
                min_val = min(min_val, lists[i].val)
            
            if min_val == float('inf'):
                break
            
            for i in range(len(lists)):
                if lists[i] == None:
                    continue
                if lists[i].val == min_val:
                    nxt.next = lists[i]
                    lists[i] = lists[i].next
                    nxt = nxt.next
        
        return dummy.next
                
        