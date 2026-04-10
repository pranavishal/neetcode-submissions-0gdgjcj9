# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(q.right, p.right)
        
        if not root:
            return isSameTree(root, subRoot)
        
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        