# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        list_heap = []
        count = 0
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(list_heap, (lists[i].val, count, lists[i]))
                count += 1

        dummy = ListNode()
        nxt = dummy

        while list_heap:
            val, node_count, node = heapq.heappop(list_heap)
            nxt.next = node
            node = node.next
            nxt = nxt.next
            
            if node:
                count += 1
                heapq.heappush(list_heap, (node.val, count, node))
              
        
        return dummy.next
                
        