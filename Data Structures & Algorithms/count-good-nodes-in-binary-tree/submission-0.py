# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodeCount(root, path_max):
            if not root:
                return 0
            
            count = 0
            if root.val >= path_max:
                path_max = root.val
                count = 1
            
            return count + goodNodeCount(root.left, path_max) + goodNodeCount(root.right, path_max)
        
        return goodNodeCount(root, float('-inf'))

