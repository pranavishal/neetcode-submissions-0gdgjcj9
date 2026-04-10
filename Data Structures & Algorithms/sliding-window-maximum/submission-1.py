from collections import defaultdict
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        val_heap = []
        current_vals = defaultdict(int)
        results = []
        for right in range(k):
            heapq.heappush(val_heap, -nums[right])
            current_vals[nums[right]] += 1
        
        results.append(-val_heap[0])

        left = 0
        for right in range(k, len(nums)):
            current_vals[nums[right]] += 1
            heapq.heappush(val_heap, -nums[right])
            current_vals[nums[left]] -= 1
            left += 1
            while current_vals[-val_heap[0]] == 0:
                heapq.heappop(val_heap)
            
            results.append(-val_heap[0])
        
        return results
        



        