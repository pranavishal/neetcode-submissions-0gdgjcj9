# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        index = 0
        val = None
        def inorderTraversal(root):
            nonlocal index
            nonlocal val

            if not root:
                return
            
            inorderTraversal(root.left)
            
            index += 1
            if index == k and val is None:
                val = root.val
            
            inorderTraversal(root.right)
        
        inorderTraversal(root)
        return val
            

        
        