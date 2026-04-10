# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, left_bound, right_bound):
            if not root:
                return True
            
            if root.val <= left_bound or root.val >= right_bound:
                return False
            
            if root.right and root.val >= root.right.val:
                return False
            
            if root.left and root.val <= root.left.val:
                return False
            

            return validate(root.left, left_bound, root.val) and validate(root.right, root.val, right_bound)
        
        return validate(root, float('-inf'), float('inf'))

