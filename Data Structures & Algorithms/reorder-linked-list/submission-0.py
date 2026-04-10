# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodeNumberMap = {}
        count = 0
        originalHead = head
        while originalHead:
            nodeNumberMap[count] = originalHead
            count += 1
            originalHead = originalHead.next
        
        print(nodeNumberMap)

        sequenceArray = [0]

        listLength = len(list(nodeNumberMap))

        for i in range(1, int(listLength / 2) + 1):
            sequenceArray.append(listLength - i)
            sequenceArray.append(i)
        
        if listLength % 2 == 0:
            sequenceArray.pop()
        
        print(sequenceArray)

        for i in range(1, len(sequenceArray)):
            head.next = nodeNumberMap[sequenceArray[i]]
            head = head.next
        
        head.next = None


        return None
        