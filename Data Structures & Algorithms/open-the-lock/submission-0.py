from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        visited = {'0000'}
        q = deque(['0000'])
        turns = 0
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr in dead_set:
                    continue
                if curr == target:
                    return turns
                neighbors = []
                for j, c in enumerate(curr):
                    c_int = int(c)
                    if c_int == 9:
                        neighbors.append(curr[0:j] + '0' + curr[j+1:])
                        neighbors.append(curr[0:j] + '8' + curr[j+1:])
                    elif c_int == 0:
                        neighbors.append(curr[0:j] + '1' + curr[j+1:])
                        neighbors.append(curr[0:j] + '9' + curr[j+1:])
                    else:
                        neighbors.append(curr[0:j] + str(c_int + 1) + curr[j+1:])
                        neighbors.append(curr[0:j] + str(c_int - 1) + curr[j+1:])
                
                for neighbor in neighbors:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)

            turns += 1

        return -1
        