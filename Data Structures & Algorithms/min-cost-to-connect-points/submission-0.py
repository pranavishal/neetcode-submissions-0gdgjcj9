class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.set_count = n

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, x):
        while x != self.parent[x]:
            # path compression 
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        
        return x
    
    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a == b:
            return False
        
        if self.rank[a] > self.rank[b]:
            self.parent[b] = a
        elif self.rank[a] < self.rank[b]:
            self.parent[a] = b
        else:
            self.parent[b] = a
            self.rank[a] += 1
        
        self.set_count -= 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dis_set = UnionFind(len(points))
        edge_weights = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, x2 = points[i]
                y1, y2 = points[j]
                weight = abs(x1 - y1) + abs(x2 - y2)
                edge_weights.append((weight, i, j))

        edge_weights.sort(key=lambda x: (x[0]))

        min_cost = 0
        for edge in edge_weights:
            if dis_set.set_count == 1:
                break
            if dis_set.union(edge[1], edge[2]):
                min_cost += edge[0]

        return min_cost

        