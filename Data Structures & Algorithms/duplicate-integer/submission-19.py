class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1. Brute Force: O(n^2)
        for i in range(len(nums)):
            for j in range(i+1, len (nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        #-----------------------------------------------

        # 2. Sorting: O(nlogn)
        #-----------------------------------------------

        # 3. Hash Set: O(n)












        #-----------------------------------------------

        # 1. Brute Force: O(n^2)

        
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        #-----------------------------------------------
        # 2. Sorting: O(nlogn)
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
        #-----------------------------------------------
        # 3. Hash Set: O(n)
        # temp = set()
        # for num in nums:
        #     if num in temp:
        #         return True    
        #     temp.add(num)
        # return False
        #-----------------------------------------------
        # 4. Hash Set Length: O(n)
        return len(set(nums)) < len(nums)
            