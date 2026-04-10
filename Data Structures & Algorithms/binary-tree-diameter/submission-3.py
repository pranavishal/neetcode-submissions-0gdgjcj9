# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter_found = 0

        def diamCheck(root):
            nonlocal max_diameter_found
            if not root:
                return 0
            
            left_tree = diamCheck(root.left)
            right_tree = diamCheck(root.right)

            max_diameter_found = max(max_diameter_found, left_tree + right_tree)
            return 1 + max(left_tree, right_tree)
        
        diamCheck(root)
        return max_diameter_found
        

        