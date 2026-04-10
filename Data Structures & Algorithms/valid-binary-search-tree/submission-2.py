# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, lower_bound, upper_bound):
            if not root:
                return True

            left_val = float('-inf')
            right_val = float('inf')
            if root.right:
                right_val = root.right.val
            if root.left:
                left_val = root.left.val
            
            if root.val <= left_val or root.val >= right_val:
                return False

            if root.val <= lower_bound or root.val >= upper_bound:
                return False
            
            return isValid(root.left, lower_bound, root.val) and isValid(root.right, root.val, upper_bound)
        
        return isValid(root, float('-inf'), float('inf'))
        