# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split list in half
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if not prev:
            return
        
        prev.next = None
        nxt = head

        # reverse second half of list
        list1 = head.next
        list2 = slow

        list2_prev = None
        list2_curr = list2

        while list2_curr:
            list2_nxt = list2_curr.next
            list2_curr.next = list2_prev
            list2_prev = list2_curr
            list2_curr = list2_nxt
        
        list2 = list2_prev

        # merge 2 lists
        list1_turn = False

        while list1 and list2:
            if list1_turn:
                nxt.next = list1
                list1 = list1.next
                list1_turn = False
            else:
                nxt.next = list2
                list2 = list2.next
                list1_turn = True
            
            nxt = nxt.next
        
        if list1:
            nxt.next = list1
        
        elif list2:
            nxt.next = list2
        

         