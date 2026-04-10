class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.count = n

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def findParent(self, x):
        p = self.parent[x]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        
        return p
    
    def union(self, x, y):
        p1, p2 = self.findParent(x), self.findParent(y)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        
        self.count -= 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        edges.sort(key=lambda x: (x[0]))
        
        uf = UnionFind(len(points))

        total_cost = 0
        for edge in edges:
            if uf.count == 1:
                break

            cost, x, y = edge
            if uf.union(x, y):
                total_cost += cost
        
        return total_cost




















