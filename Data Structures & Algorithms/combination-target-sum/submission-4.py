class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #backtracking
        res = []
        def backtrack(start, subsets):
            # Add current chocie to result (base case)
            if sum(subsets) > target:
                return
            if sum(subsets) == target:
                res.append(subsets[:]) #[:] added for making a copy
            # For each remaining option
                # Make the choice (add to current)
                # Recurse with updated state
                # Undo the choice (backtrack)
            for i in range(start, len(nums)):
                subsets.append(nums[i])
                backtrack(i, subsets)
                subsets.pop()

        backtrack(0, [])
        return res


