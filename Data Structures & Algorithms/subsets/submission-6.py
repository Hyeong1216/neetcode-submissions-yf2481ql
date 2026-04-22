class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #iterative
        # res = [[]]
        # for num in nums:
        #     temp = []
        #     for i in range(len(res)):
        #         temp.append(res[i] + [num])
        #     res.extend(temp)
        # return res

        # backtracking
        res = []
        def bt(start, subset):
            res.append(subset[:])
            for i in range(start, len(nums)):
                subset.append(nums[i])
                bt(i+1, subset)
                subset.pop()


        bt(0, [])
        return res