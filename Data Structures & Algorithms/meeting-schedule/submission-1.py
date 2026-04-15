"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        newIntervals = []
        for i in range(len(intervals)):
            newIntervals.append([intervals[i].start, intervals[i].end])

        newIntervals.sort(key=lambda x:(x[0], x[1]))
        last_end = newIntervals[0][1] if newIntervals else not None
        for i in range(1, len(newIntervals)):
            if newIntervals[i][0] < last_end: #when overlap
                return False
            else: #when not overlap, update last_end
                last_end = newIntervals[i][1]
        
        return True