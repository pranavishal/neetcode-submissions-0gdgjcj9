# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([])

        queue.append(root)
        allLevelList = []
        while queue:
            levelList = []
            for i in range(len(queue)):
                currentNode = queue.popleft()
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                levelList.append(currentNode.val)
            allLevelList.append(levelList)
        
        return allLevelList
        