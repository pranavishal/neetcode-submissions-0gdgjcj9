import heapq
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        heap = []
        counter = Counter(hand)
        for key, value in counter.items():
            heapq.heappush(heap, [key, value])
        
        while heap:
            print(heap)
            vals = []
            for i in range(groupSize):
                if not heap:
                    return False
                vals.append(heapq.heappop(heap))

            min_amount = vals[0][1]
            curr_val = vals[0][0]
            for j in range(1, len(vals)):
                if vals[j][1] < min_amount or vals[j][0] != curr_val + 1:
                    return False
                curr_val += 1
            
            for x in range(1, len(vals)):
                vals[x][1] -= min_amount
                if vals[x][1] > 0:
                    heapq.heappush(heap, vals[x])
        
        return True

