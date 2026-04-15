class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force: O(n^2)
        # res = []
        # for i in range(len(temperatures)):
        #     count = 0

        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             count = j-i
        #             break
        #     res.append(count)
        # return res

        # Stack
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures) :
            while stack and temperatures[stack[-1]] < temperatures[i] :
                prev_index = stack.pop()
                res[prev_index] = i - prev_index

            stack.append(i)
        return res









