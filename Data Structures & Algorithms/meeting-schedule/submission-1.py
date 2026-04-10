"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if len(intervals) == 0:
            return True
        prev_ending = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < prev_ending:
                return False
            prev_ending = intervals[i].end
        return True
