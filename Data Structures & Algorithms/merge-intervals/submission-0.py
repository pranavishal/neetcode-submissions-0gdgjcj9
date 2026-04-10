class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i, interval in enumerate(intervals):
            prev = result.pop()
            if prev[0] <= interval[1] and interval[0] <= prev[1]:
                max_val = max(interval[1], prev[1])
                result.append([prev[0], max_val])
            else:
                result.append(prev)
                result.append(interval)
        
        return result
