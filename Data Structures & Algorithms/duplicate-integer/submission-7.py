class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #brute force
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        #sorting
        # nums.sort()
        # for i in range(0, len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        #hashset
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False          



