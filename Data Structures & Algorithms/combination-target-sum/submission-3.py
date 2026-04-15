class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(current_combination, current_sum, index):
            if current_sum == target:
                result.append(current_combination[:])
                return
            
            if current_sum > target:
                return

            for i in range(index, len(nums)):
                current_combination.append(nums[i])
                backtrack(current_combination, current_sum + nums[i], i)
                current_combination.pop()
        backtrack([], 0, 0)
        return result