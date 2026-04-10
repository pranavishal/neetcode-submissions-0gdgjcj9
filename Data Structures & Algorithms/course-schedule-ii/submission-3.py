from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for req in prerequisites:
            a, b = req
            adj_list[b].append(a)
        
        q = deque()

        # 0 -> unvisited, 1 -> visiting, 2 -> visited
        colors = [0] * numCourses
        def dfs(node):
            colors[node] = 1
            for neighbor in adj_list[node]:
                if colors[neighbor] == 1:
                    return False
                if colors[neighbor] == 0:
                    if not dfs(neighbor):
                        return False

            q.appendleft(node)
            colors[node] = 2
            return True
        
        for i in range(numCourses):
            if colors[i] == 0:
                if not dfs(i):
                    print(i)
                    return []
        
        return list(q)
        
        