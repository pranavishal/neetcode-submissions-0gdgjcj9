import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        def hoursNeeded(k):
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / k)
            return hours
        
        min_k = right
        while left <= right:
            mid = (left + right) // 2
            
            needed = hoursNeeded(mid)
            if needed <= h:
                min_k = min(min_k, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return min_k
                
