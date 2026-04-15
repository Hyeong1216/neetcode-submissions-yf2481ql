class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Approach 1: Greedy by End Time
        # Time: O(n log n) | Space: O(1)
        intervals.sort(key=lambda x: (x[1], x[0]))
        # print(intervals)
        last_end = float('-inf')
        result = []

        for i in range(len(intervals)):
            if intervals[i][0] >= last_end:
                result.append(intervals[i])
                last_end = intervals[i][1]


        return len(intervals) - len(result)



        # Approach 2: Greedy by Overlap Count
        # Time: O(n log n) | Space: O(1)
