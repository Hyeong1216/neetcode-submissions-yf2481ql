class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []

        for i in range(len(intervals)):
            if result and intervals[i][0] <= result[-1][1]:
                curr_start = min(intervals[i][0], result[-1][0])
                curr_end = max(intervals[i][1], result[-1][1])
                result[-1] = [curr_start, curr_end]
            else:
                result.append(intervals[i])


        return result