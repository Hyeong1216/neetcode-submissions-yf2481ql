class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(start, subset):
            if sum(subset) > target:
                return

            if sum(subset) == target:
                if sorted(subset) not in res:
                    res.append(sorted(subset[:]))
                    return

            for i in range(start, len(nums)):
                subset.append(nums[i])
                bt(i+1, subset)
                subset.pop()

        bt(0, [])
        return res