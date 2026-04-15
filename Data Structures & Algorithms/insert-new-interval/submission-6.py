class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 1. Three phase approach: O(n)
        # phase 1: add intervals that end before newInterval starts (no overlap)
        # phase 2: Merge newInterval with all overlapping intervals
        # phase 3: Add intervals that start after merged interval ends (no onverlap)
        # result = []
        # i = 0

        # # phase 1
        # while i < len(intervals) and intervals[i][1] < newInterval[0]:
        #     result.append(intervals[i])
        #     i += 1
        

        # # phase 2
        # if i < len(intervals): # still have intervals to check
        #     merged_start = newInterval[0]
        #     merged_end = newInterval[1]

        #     while i < len(intervals) and intervals[i][0] <= merged_end:
        #         merged_start = min(merged_start, intervals[i][0])
        #         merged_end = max(merged_end, intervals[i][1])
        #         i +=1

        #     result.append([merged_start, merged_end])

        # else: # no more new intervals to check
        #     result.append(newInterval)

        # # phase 3
        # while i < len(intervals):
        #     result.append(intervals[i])
        #     i += 1

        # return result
        #---------------------------------------------------------------------------
        # 2. Insert-then-Merge
        inserted = False
        insert_index = 0
        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0]:
                intervals.insert(i, newInterval)
                inserted = True
                insert_index = i
                break
        if not inserted:
            intervals.append(newInterval)
            insert_index = len(intervals) - 1

        left = insert_index
        right = insert_index

        while left > 0 and intervals[left-1][1] >= intervals[insert_index][0]:
            left -= 1
        
        while right < len(intervals) -1 and intervals[right+1][0] <= intervals[insert_index][1]:
            right += 1
        
        merged_start = intervals[left][0]
        merged_end = intervals[left][1]
        for j in range(left, right + 1):
            merged_end = max(merged_end, intervals[j][1])
        
        intervals[left:right+1] = [[merged_start, merged_end]]

        return intervals
