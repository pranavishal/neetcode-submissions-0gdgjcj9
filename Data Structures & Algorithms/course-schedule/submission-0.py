class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjacencyList = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adjacencyList[b].append(a)
        
        # pred, color, disc, finish, time, isDag

        pred = [0] * numCourses
        color = [0] * numCourses
        discovery = [0] * numCourses
        finish = [0] * numCourses
        time = 0
        isDag = True

        def dfs():
            for i in range(len(adjacencyList)):
                if color[i] == 0:
                    dfsVisit(i)
        
        def dfsVisit(node):
            #tell python these nodes live 1 level up
            nonlocal pred, color, discovery, finish, time, isDag

            # node is discovered
            color[node] = 1
            #increment time
            time += 1
            #set discovery time
            discovery[node] = time

            for neighbor in adjacencyList[node]:
                # undiscovered node
                if color[neighbor] == 0:
                    pred[neighbor] = node
                    dfsVisit(neighbor)
                # discovered node that's not completed, no longer a dag
                if color[neighbor] == 1:
                    isDag = False
            
            color[node] = 2
            time += 1
            finish[node] = time
        
        dfs()

        return isDag
                