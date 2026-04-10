# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        is_same = True
        def isSame(p, q):
            nonlocal is_same
            if (p is None and q is not None) or (p is not None and q is None):
                is_same = False
                return
            
            if not p:
                return
            
            if p.val != q.val:
                is_same = False
                return

            isSame(p.left, q.left)
            isSame(p.right, q.right) 

        isSame(p, q)
        return is_same