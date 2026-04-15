class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 1. Three phase approach
        # phase 1: add intervals that end before newInterval starts (no overlap)
        # phase 2: Merge newInterval with all overlapping intervals
        # phase 3: Add intervals that start after merged interval ends (no onverlap)
        result = []
        i = 0

        # phase 1
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        

        # phase 2
        if i < len(intervals): # still have intervals to check
            merged_start = newInterval[0]
            merged_end = newInterval[1]

            while i < len(intervals) and intervals[i][0] <= merged_end:
                merged_start = min(merged_start, intervals[i][0])
                merged_end = max(merged_end, intervals[i][1])
                i +=1

            result.append([merged_start, merged_end])

        else: # no more new intervals to check
            result.append(newInterval)

        # phase 3
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result