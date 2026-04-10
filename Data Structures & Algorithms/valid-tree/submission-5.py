from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(set)
        colors = [0] * n
        pred = [None] * n
        for edge in edges:
            a, b = edge[0], edge[1]
            adj_list[a].add(b)
            adj_list[b].add(a)
        valid_tree = False
        def dfs(node):
            colors[node] = 1

            for edge in adj_list[node]:
                if colors[edge] == 1 and pred[node] != edge:
                    return False
                if colors[edge] == 0:
                    pred[edge] = node
                    if not dfs(edge):
                        return False
            
            colors[node] = 2
            return True
        
        if not dfs(0):
            return False
        
        return all(color == 2 for color in colors)

