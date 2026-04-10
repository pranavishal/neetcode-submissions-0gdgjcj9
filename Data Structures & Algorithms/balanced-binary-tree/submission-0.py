# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            
            leftHeight = 0
            rightHeight = 0

            if root.left:
                leftHeight = height(root.left)
            
            if root.right:
                rightHeight = height(root.right)
            
            return 1 + max(height(root.left), height(root.right))
        
        if not root:
            return True
        
        if height(root) == 1:
            return True
        
        else:
            return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    

        