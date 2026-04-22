class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #iterative
        res = [[]]
        for num in nums:
            temp = []
            for i in range(len(res)):
                temp.append(res[i] + [num])
            res.extend(temp)
        return res
