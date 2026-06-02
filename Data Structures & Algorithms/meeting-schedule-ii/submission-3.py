"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Questions
        # 1. Can intervals be mepty?

        # room = 1 initially, if find overlap + room
        intervals.sort(key=lambda x: x.start)

        # Initialize a min-heap to store the end times of meetings
        # that are currently occupying the room.
        # The heap will always give us the eraliest ending meeting.
        room_end_times = []

        # Initialize a variable to keep track of the maximum number of rooms needed.
        min_rooms = 0

        for interval in intervals:
            start = interval.start
            end = interval.end

            # if the heap is not empty and the current meeting's start time
            # is greater than or equal to the earlisest ending meeting in our rooms:
            # this means a room has become available.
            if room_end_times and start >= room_end_times[0]:        
                heapq.heappop(room_end_times)

            
            heapq.heappush(room_end_times, end)
            min_rooms = max(min_rooms, len(room_end_times))




        return min_rooms