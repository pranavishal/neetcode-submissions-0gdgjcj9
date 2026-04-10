class UnionFind:
    def __init__(self, x):
        self.par = {}
        self.rank = {}
        self.count = x

        for i in range(1, x + 1):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, x):
        p = self.par[x]
        while p != self.par[p]:
            #path compression
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        
        self.count -= 1

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        largest = float('-inf')
        for edge in edges:
            x, y = edge
            largest = max(x, y, largest)
        
        dis_set = UnionFind(largest)

        for edge in edges:
            x, y = edge
            if not dis_set.union(x, y):
                return edge

        
        