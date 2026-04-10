"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone_map = {}
        def dfs(node):
            if not node:
                return None
            
            if node in clone_map:
                return clone_map[node]
            
            new_node = Node(node.val)
            clone_map[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            
            return clone_map[node]
        
        return dfs(node)
        