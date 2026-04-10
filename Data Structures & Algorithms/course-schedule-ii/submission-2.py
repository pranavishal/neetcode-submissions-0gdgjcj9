from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for req in prerequisites:
            x, y = req
            adj_list[y].append(x)
        
        color = [0] * numCourses
        q = deque()

        def dfs(node):
            color[node] = 1

            for adj in adj_list[node]:
                if color[adj] == 1:
                    return False
                if color[adj] == 0:
                    if not dfs(adj):
                        return False
            
            q.appendleft(node)
            color[node] = 2
            return True
        
        for i in range(numCourses):
            if color[i] == 0:
                if not dfs(i):
                    return []
        
        return list(q)
        
