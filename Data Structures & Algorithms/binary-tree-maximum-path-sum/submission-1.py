# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        def maxSum(root):
            nonlocal max_sum
            if not root:
                return 0
            
            left_sum = maxSum(root.left)
            right_sum = maxSum(root.right)
            
            total_sum = root.val
            if left_sum > 0:
                total_sum += left_sum
            if right_sum > 0:
                total_sum += right_sum
            
            max_sum = max(total_sum, max_sum)

            return root.val + max(left_sum, right_sum, 0)
        
        maxSum(root)
        return max_sum
            
            
        