class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        def bt(start, subset):
            res.append(subset[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                bt(i + 1, subset)
                subset.pop()

        bt(0, [])
        return res
