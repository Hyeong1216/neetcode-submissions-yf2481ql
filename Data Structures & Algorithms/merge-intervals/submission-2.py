class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Questions
        # 1. Can interval be empty?
        # 2. are the intervals already sorted?


        # Approach 1: sort + single pass
        # Time: O(n log n) | Space: O(1) excluding output
        intervals.sort(key=lambda x: x[0])
        result = []
        
        for i in range(len(intervals)):
            if result and intervals[i][0] <= result[-1][1]:
                start = min(intervals[i][0], result[-1][0])
                end = max(intervals[i][1], result[-1][1])
                result[-1] = [start, end]

            else:
                result.append(intervals[i])


        return result







        # Approach 2: sort + two pointers