from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        curr_cycle = 1
        task_heap = []
        for key, value in counter.items():
            heapq.heappush(task_heap, (-value, key))
        
        cooldown = deque()

        # ["X","X","Y","Y"]
        # heap = ["]
        # cooldown = ["X, 1, 3", "Y, 1, 4"]
        while task_heap or cooldown:
            while cooldown and cooldown[0][2] <= curr_cycle:
                task, count, cycle = cooldown.popleft()
                heapq.heappush(task_heap, (-count, task))
            
            if task_heap:
                count, task = heapq.heappop(task_heap)
                count = abs(count)
                if (count - 1 > 0):
                    cooldown.append((task, count - 1, curr_cycle + n + 1))
                curr_cycle += 1
            else:
                curr_cycle = cooldown[0][2]
        
        return curr_cycle - 1




        