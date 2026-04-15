class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 1. Brute force
        def backtrack(index):
            # Base case: reached or passed the end
            if index >= len(nums)-1:
                return True

            # Base case: out of bounds or no moves possible
            if index >= len(nums) or nums[index] == 0:
                return False
            
            for jump_length in range(1, nums[index]+1):
                next_index = index + jump_length
                if backtrack(next_index):
                    return True
                
            return False
        return backtrack(0)