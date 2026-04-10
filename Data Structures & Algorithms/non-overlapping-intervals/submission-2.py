class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        print(intervals)
        result = [intervals[0]]
        removed = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < result[-1][1]:
                prev = result.pop()
                if intervals[i][1] < prev[1]:
                    result.append(intervals[i])
                else:
                    result.append(prev)
                removed += 1
            else:
                result.append(intervals[i])
        
        return removed