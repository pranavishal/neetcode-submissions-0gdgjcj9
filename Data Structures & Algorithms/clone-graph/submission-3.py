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

        def dfs(n):
            if n not in clone_map:
                new_node = Node(val=n.val)
                clone_map[n] = new_node
                for neighbor in n.neighbors:
                    clone_map[n].neighbors.append(dfs(neighbor))

            return clone_map[n]
        
        if not node:
            return None
            
        return dfs(node)