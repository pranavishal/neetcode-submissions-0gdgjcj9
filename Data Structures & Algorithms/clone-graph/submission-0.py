"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        nodeMap = {}
        return self.dfs(node, nodeMap)

    def dfs(self, node, nodeMap):
        if node in nodeMap:
            return nodeMap[node]
        
        cloneNode = Node(node.val)
        nodeMap[node] = cloneNode
        for neighbor in node.neighbors:
            cloneNode.neighbors.append(self.dfs(neighbor, nodeMap))
        
        return cloneNode
        


        