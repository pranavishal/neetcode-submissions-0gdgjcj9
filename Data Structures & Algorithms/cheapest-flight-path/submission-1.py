class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = {}
        for i in range(n):
            if i == src:
                prices[i] = 0
            else:
                prices[i] = float('inf')
        
        temp = prices.copy()
        
        for i in range(k + 1):
            for flight in flights:
                home, away, cost = flight
                if prices[home] + cost < temp[away]:
                    temp[away] = prices[home] + cost
            
            prices = temp.copy()
        
        if prices[dst] == float('inf'):
            return -1
        return prices[dst]
        