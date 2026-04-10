import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # preprocessing
        for i in range(len(tasks)):
            tasks[i].append(i)
        
        tasks.sort(key=lambda x: (x[0], x[1], x[2]))
        tasks.reverse()
        # [[1, 4, 0], [2, 1, 2], [3, 3, 2]]
        # [[3, 3, 2], [2, 1, 2], [1, 4, 0]]

        # main loop setup
        task_len = len(tasks)
        curr_time = 1

        #heap
        task_heap = []

        #return value
        result = []
        

        while task_heap or tasks:
            while tasks and tasks[-1][0] <= curr_time:
                enqueue_time, processing_time, index = tasks.pop()
                heapq.heappush(task_heap, (processing_time, index))
            
            if task_heap:
                proc_time, index = heapq.heappop(task_heap)
                result.append(index)
                curr_time += proc_time
            else:
                # if nothing available under current time, move time to beginning of next
                # possible task
                curr_time = tasks[-1][0]
                
        return result

        

