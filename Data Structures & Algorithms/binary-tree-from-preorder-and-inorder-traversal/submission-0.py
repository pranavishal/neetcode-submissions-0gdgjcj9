# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre = 0
        def build(preorder, inorder):
            nonlocal pre
            if len(inorder) == 0:
                return None
            
            
            inorder_index = inorder.index(preorder[pre])
            pre += 1
            root = TreeNode(val=inorder[inorder_index])

            root.left = build(preorder, inorder[:inorder_index])
            root.right = build(preorder, inorder[inorder_index+1:])
            return root

        return build(preorder, inorder)       