class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            if not stack or temperatures[stack[-1]] > curr_temp:
                stack.append(i)
                continue
            
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day_index = stack.pop()
                res[prev_day_index] = i - prev_day_index
            stack.append(i)

            

        return res







































# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         res = [0] * len(temperatures)
#         stack = []
#         for i, temp in enumerate(temperatures):
#             while stack and temperatures[stack[-1]] < temperatures[i]:
#                 prev_index = stack.pop()
#                 res[prev_index] = i - prev_index
#             stack.append(i)


#         return res
#         #----------------
#         # res = [0] * len(temperatures)
#         # stack = []

#         # for i, temp in enumerate(temperatures):
#         #     while stack and temperatures[stack[-1]] < temperatures[i]:
#         #         prev_index = stack.pop()
#         #         res[prev_index] = i - prev_index

#         #     stack.append(i)
#         # return res
        
#         #----------------
#         # brute force
#         # res = []
#         # for i in range(len(temperatures)):
#         #     count = 0
#         #     for j in range(i+1, len(temperatures)):
#         #         if temperatures[i] < temperatures[j]:
#         #             count = j - i
#         #             break
#         #     res.append(count)

#         # return res