class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. sort + single pass
        intervals.sort(key=lambda x: x[0])
        result = []

        for i in range(len(intervals)):
            if result and result[-1][1] >= intervals[i][0]:
                start = min(result[-1][0], intervals[i][0])
                end = max(result[-1][1], intervals[i][1])
                result[-1] = [start, end]
            
            else:
                result.append(intervals[i])


        return result
















# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         # Questions
#         # 1. Can interval be empty?
#         # 2. are the intervals already sorted?


#         # Approach 1: sort + single pass
#         # Time: O(n log n) | Space: O(1) excluding output
#         intervals.sort(key=lambda x: x[0])
#         result = []
        
#         for i in range(len(intervals)):
#             if result and intervals[i][0] <= result[-1][1]:
#                 start = min(intervals[i][0], result[-1][0])
#                 end = max(intervals[i][1], result[-1][1])
#                 result[-1] = [start, end]

#             else:
#                 result.append(intervals[i])


#         return result
#         # Time: O(N log N) — sorting dominates
#         # Space: O(1) — excluding output array





#         # Approach 2: sort + two pointers