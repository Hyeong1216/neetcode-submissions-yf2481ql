class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        print(candidates)
        def bt(start, curr, remain):
            if remain == 0:
                res.append(curr[:])
            if remain < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                bt(i+1, curr, remain-candidates[i])
                curr.pop()



        bt(0, [], target)
        return res


































# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         candidates.sort()
#         def bt(start, subset, remain):
#             if remain == 0:
#                 res.append(subset[:])
#                 return
#             if remain < 0:
#                 return
            
#             for i in range(start, len(candidates)):
#                 if i > start and candidates[i] == candidates[i-1]:
#                     continue
#                 subset.append(candidates[i])
#                 bt(i+1, subset, remain-candidates[i])
#                 subset.pop()


        
#         bt(0, [], target)

#         return res