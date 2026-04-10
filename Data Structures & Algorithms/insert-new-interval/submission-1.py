class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        result = []

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        curr_interval = newInterval
        while i < n and intervals[i][0] <= curr_interval[1]:
            min_val = min(intervals[i][0], curr_interval[0])
            max_val = max(intervals[i][1], curr_interval[1])
            curr_interval = [min_val, max_val]
            i += 1
        
        result.append(curr_interval)
        
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
        