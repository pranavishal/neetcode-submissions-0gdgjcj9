# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        bfsDeque = deque([root])
        rightView = []

        while bfsDeque:
            levelLength = len(bfsDeque)
            newDeque = deque([])
            for i in range(levelLength):
                if i == levelLength - 1:
                    rightView.append(bfsDeque[i].val)
                if bfsDeque[i].left:
                    newDeque.append(bfsDeque[i].left)
                
                if bfsDeque[i].right:
                    newDeque.append(bfsDeque[i].right)
            
            bfsDeque = newDeque.copy()
        
        print()
        return rightView





        
        