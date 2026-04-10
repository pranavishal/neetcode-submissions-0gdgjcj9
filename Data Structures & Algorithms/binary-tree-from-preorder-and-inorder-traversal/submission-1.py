# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre = 0
        inorder_map = defaultdict(int)
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i
            
        def build(left, right):
            nonlocal pre
            if left > right:
                return None
            
            inorder_index = inorder_map[preorder[pre]]
            pre += 1
            root = TreeNode(val=inorder[inorder_index])

            root.left = build(left, inorder_index - 1)
            root.right = build(inorder_index + 1, right)
            return root

        return build(0, len(inorder) - 1)       