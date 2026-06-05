"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals_new = sorted(intervals, key=lambda x:x.start)
        for i in range(1,len(intervals_new)):
            if intervals_new[i].start < intervals_new[i-1].end:
                return False
        return True
