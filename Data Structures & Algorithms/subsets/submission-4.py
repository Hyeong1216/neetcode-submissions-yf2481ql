class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # iterative
        # result = [[]]
        # for num in nums:
        #     temp = []
        #     for subset in result:
        #         temp.append(subset + [num])
        #     result.extend(temp)
        # return result
        #------------------------------------------------
        # backtracking
        # res = []
        # def backtrack(start, subsets):
        #     # Add current chocie to result (base case)
        #     res.append(subsets[:]) #[:] added for making a copy
            
        #     # For each remaining option
        #         # Make the choice (add to current)
        #         # Recurse with updated state
        #         # Undo the choice (backtrack)
        #     for i in range(start, len(nums)):
        #         subsets.append(nums[i])
        #         backtrack(i+1, subsets)
        #         subsets.pop()

        # backtrack(0, [])
        # return res


        res = []
        def bt(start, subset):
            res.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])
                bt(i+1, subset)
                subset.pop()
        bt(0, [])
        return res