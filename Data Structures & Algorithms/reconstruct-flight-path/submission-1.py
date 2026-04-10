from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for tick in tickets:
            src, dest = tick
            adj_list[src].append(dest)
        
        for key, value in adj_list.items():
            value.sort()
        
        res = ["JFK"]
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            
            temp = adj_list[node].copy()
            for i, dest in enumerate(temp):
                adj_list[node].pop(i)
                res.append(dest)
                if dfs(dest):
                    return True
                res.pop()
                adj_list[node].insert(i, dest)
            
            return False
        
        dfs("JFK")
        return res
                
        