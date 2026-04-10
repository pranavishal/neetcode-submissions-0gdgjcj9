from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        colors = [0] * numCourses
        adj_list = defaultdict(list)
        for prereq in prerequisites:
            a, b = prereq
            adj_list[b].append(a)
        
        can_complete = True

        def dfs(node):
            nonlocal can_complete
            colors[node] = 1

            for neighbor in adj_list[node]:
                if colors[neighbor] == 1:
                    can_complete = False
                if colors[neighbor] == 0:
                    dfs(neighbor)
            
            colors[node] = 2
        
        for i in range(numCourses):
            if colors[i] == 0:
                dfs(i)
        
        return can_complete
        