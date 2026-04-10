from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num_components = 0
        visited = set()
        adj_list = defaultdict(list)
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        def bfs(node):
            q = deque([node])
            while q:
                curr = q.popleft()
                for adj in adj_list[curr]:
                    if adj not in visited:
                        visited.add(adj)
                        q.append(adj)
            
        
        for i in range(n):
            if i not in visited:
                num_components += 1
                visited.add(i)
                bfs(i)
        
        return num_components
        
        
        