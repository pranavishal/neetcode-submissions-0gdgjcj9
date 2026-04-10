# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is either
        # 0 if node has no children
        # max(maximumDepth of left + maximum depth of right + 2, diameterOfBinaryTree(root.left), diameterOfBinaryTree(root.right))

        def maximumDepth(root):
            if not root:
                return 0
            
            return 1 + max(maximumDepth(root.left), maximumDepth(root.right))

        def treeDiameter(root):
            if not root:
                return 0
            
            return max(maximumDepth(root.left) + maximumDepth(root.right), treeDiameter(root.left), treeDiameter(root.right))
        
        return treeDiameter(root)
            
        


        