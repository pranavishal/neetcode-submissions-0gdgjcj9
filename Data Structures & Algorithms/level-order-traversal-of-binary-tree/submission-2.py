# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        q = deque()
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                if not curr:
                    continue
                q.append(curr.left)
                q.append(curr.right)
                level.append(curr.val)
            
            if level:
                levels.append(level)
        
        return levels

        