# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def dfs(root): 
            nonlocal best     
            if not root:
                return 0
            
            maxLeft = 0
            maxRight = 0
            if root.left:
                maxLeft = 1 + dfs(root.left)
            
            if root.right:
                maxRight = 1 + dfs(root.right)
            

            best = max(best, maxLeft + maxRight)
            return max(maxLeft, maxRight)
            


            
        dfs(root)
        return best
        