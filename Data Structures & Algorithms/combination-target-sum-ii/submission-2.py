class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def bt(start, current_sum, subset):
            if current_sum > target:
                return

            if current_sum == target:
                res.append(subset[:])
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                bt(i+1, current_sum + nums[i], subset)
                subset.pop()

        bt(0, 0, [])
        return res