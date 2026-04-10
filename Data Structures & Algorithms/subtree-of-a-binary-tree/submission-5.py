# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if bool(p) != bool(q):
                return False
            
            if not p:
                return True
            
            if p.val != q.val:
                return False
            
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        
        def subCheck(root, subRoot):
            if not subRoot:
                return True
            
            if not root:
                return False
            
            is_root = root.val == subRoot.val and isSame(root, subRoot)
            
            return is_root or subCheck(root.left, subRoot) or subCheck(root.right, subRoot)
        
        return subCheck(root, subRoot)

        