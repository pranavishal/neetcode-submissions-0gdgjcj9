from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        colors = [0] * numCourses
        adj_list = defaultdict(list)
        for prereq in prerequisites:
            a, b = prereq
            adj_list[b].append(a)

        def dfs(node):
            colors[node] = 1

            for neighbor in adj_list[node]:
                if colors[neighbor] == 1:
                    return False
                if colors[neighbor] == 0:
                     if dfs(neighbor) == False:
                        return False
            
            colors[node] = 2
            return True
        
        for i in range(numCourses):
            if colors[i] == 0:
                if dfs(i) == False:
                    return False
        
        return True
