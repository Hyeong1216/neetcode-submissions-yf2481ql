class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Approach 1: Greedy by End Time
        # Time: O(n log n) | Space: O(1)
        # intervals.sort(key=lambda x: (x[1], x[0]))
        # last_end = float('-inf')
        # result = []

        # for i in range(len(intervals)):
        #     if last_end <= intervals[i][0]: # no onverlap
        #         result.append(intervals[i])
        #         last_end = intervals[i][1]

        # return len(intervals) - len(result)
        #-----------------------------------------------------------------
        # Approach 2: Greedy by Overlap Count
        # Time: O(n log n) | Space: O(1)
        intervals.sort(key=lambda x:(x[0], x[1]))

        if not intervals:
            return 0
        
        removals = 0
        current_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < current_end:
               removals += 1
               current_end = min(current_end, intervals[i][1]) 
            else:
                current_end = intervals[i][1]



        return removals

