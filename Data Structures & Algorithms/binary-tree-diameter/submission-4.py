# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_len = float('-inf')

        def diameter(root):
            nonlocal max_len
            if not root:
                return 0
            
            left_len = diameter(root.left)
            right_len = diameter(root.right)

            max_len = max(max_len, left_len + right_len)

            return max(left_len + 1, right_len + 1)
        
        diameter(root)
        return max_len




        