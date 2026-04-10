class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        result = []
        first_interval_index = float('inf')
        last_interval_index = float('-inf')
        insert_start = float('inf')
        insert_end = float('-inf')
        for i, interval in enumerate(intervals):
            if newInterval[0] <= interval[1] and interval[0] <= newInterval[1]:
                first_interval_index = min(first_interval_index, i)
                last_interval_index = max(last_interval_index, i)
                insert_start = min(insert_start, newInterval[0], interval[0])
                insert_end = max(insert_end, newInterval[1], interval[1])
        
        inserted = False
        if first_interval_index == float('inf') and last_interval_index == float('-inf'):
            found = False
            for i, interval in enumerate(intervals):
                if newInterval[0] < interval[0]:
                    intervals.insert(i, newInterval)
                    found = True
                    break
            if not found:
                intervals.append(newInterval)

            return intervals
        
        if first_interval_index == float('-inf'):
            intervals.append(newInterval)
            return intervals

        for i, interval in enumerate(intervals):
            if i >= first_interval_index and i <= last_interval_index:
                if not inserted:
                    result.append([insert_start, insert_end])
                    inserted = True
            else:
                result.append(interval)

        return result
