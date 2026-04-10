import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, -num)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        pushed_vals = []
        for i in range(self.k):
            pushed_vals.append(-heapq.heappop(self.heap))
        
        k_largest = pushed_vals[-1]
        for num in pushed_vals:
            heapq.heappush(self.heap, -num)
        return k_largest

        
