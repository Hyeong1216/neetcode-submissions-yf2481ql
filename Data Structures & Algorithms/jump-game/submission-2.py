class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 1. Brute force: Time Complexity: O(2^n)
        # def backtrack(index):
        #     # Base case: reached or passed the end
        #     if index >= len(nums)-1:
        #         return True

        #     # Base case: out of bounds or no moves possible
        #     if index >= len(nums) or nums[index] == 0:
        #         return False
            
        #     for jump_length in range(1, nums[index]+1):
        #         next_index = index + jump_length
        #         if backtrack(next_index):
        #             return True
                
        #     return False
        # return backtrack(0)
        #-----------------------------------------------------------------------
        # 2. Greedy approach:
        furthest_reach = 0
        for i in range(len(nums)):
            # Check if current position if reachable
            if i > furthest_reach:
                return False
            
            furthest_reach = max(furthest_reach, i+nums[i])
            
            if furthest_reach >= len(nums) - 1:
                return True
        return True