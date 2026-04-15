class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Approach 1: Sort + Single Pass
        # Time: O(n log n) | Space: O(1) excluding output
        # intervals.sort(key=lambda x: x[0])
        # result = []

        # for i in range(len(intervals)):
        #     if result and intervals[i][0] <= result[-1][1]:
        #         curr_start = min(intervals[i][0], result[-1][0])
        #         curr_end = max(intervals[i][1], result[-1][1])
        #         result[-1] = [curr_start, curr_end]
        #     else:
        #         result.append(intervals[i])

        # return result
        #-------------------------------------------------
        # Approach 2: Sort + Two Pointers
        # Time: O(n log n) | Space: O(1) excluding output
        intervals.sort(key=lambda x: x[0])
        result = []
        
        i = 0
        while i < len(intervals):
            merged_start = intervals[i][0]
            merged_end = intervals[i][1]
            # intervals[i][0] <= result[-1][1]:
            while i + 1 <len(intervals) and intervals[i+1][0] <= merged_end:
                i+=1
                merged_end = max(merged_end, intervals[i][1])
            result.append([merged_start, merged_end])
            i+=1

                


        return result