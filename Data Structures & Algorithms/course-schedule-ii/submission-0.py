class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create the adjacency list
        adjacencyList = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adjacencyList[b].append(a)
        
        # predecessor variable, which node discovered said node
        pred = [0] * numCourses

        # color nodes, 0 -> unvisited, 1 -> visited, 2 -> done being visited
        color = [0] * numCourses

        # disc and finish times
        disc = [0] * numCourses
        finish = [0] * numCourses

        # time variable
        time = 0

        #isDAG
        isDag = True

        # course ordering
        courseOrdering = []

        def dfs():
            for i in range(len(color)):
                if color[i] == 0:
                    dfsVisit(i)
        
        def dfsVisit(node):
            # tell python about higher scoped variables
            nonlocal pred, color, disc, finish, time, isDag, courseOrdering

            color[node] = 1
            time += 1
            disc[node] = time

            for neighbor in adjacencyList[node]:
                # undiscovered nodes
                if color[neighbor] == 0:
                    pred[neighbor] = node
                    dfsVisit(neighbor)
                
                # detecting cycles
                if color[neighbor] == 1:
                    isDag = False
            
            color[node] = 2
            time += 1
            finish[node] = time
            courseOrdering.append(node)
            print(courseOrdering)
        
        dfs()

        if not isDag:
            return []
        
        else:
            courseOrdering.reverse()
            return courseOrdering
            

        

        