class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Brute force
        #--------------------------------------------------

        # 2. Sorting
        #--------------------------------------------------

        # 3. Hash Map (Two pass)

        #--------------------------------------------------
        # 4. Hash Map (One Pass)
        Map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in Map:
                return [Map[diff], i]
            Map[nums[i]] = i
        



        #--------------------------------------------------




        # Map = {}
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in Map:
        #         return [Map.get(diff), i]
        #     Map[nums[i]] = i
        
        