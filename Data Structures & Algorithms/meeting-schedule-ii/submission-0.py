"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: (x.start, x.end))
        meeting_heap = []
        days_needed = 0
        for interval in intervals:
            if len(meeting_heap) == 0 or meeting_heap[0] > interval.start:
                days_needed += 1
            else:
                heapq.heappop(meeting_heap)
                
            heapq.heappush(meeting_heap, interval.end)

        return days_needed


        