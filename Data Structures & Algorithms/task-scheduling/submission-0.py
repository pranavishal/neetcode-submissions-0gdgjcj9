from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        task_heap = []
        task_queue = deque([])
        for key, value in counter.items():
            heapq.heappush(task_heap, -value)
        
        time = 0
        while task_heap or task_queue:
            time += 1
            if task_heap:
                val = heapq.heappop(task_heap)
                val += 1
                
                if val < 0:
                    task_queue.append((val, time + n))
            
            while task_queue and task_queue[0][1] <= time:
                q_val, q_time = task_queue.popleft()
                heapq.heappush(task_heap, q_val)

        return time
        





        