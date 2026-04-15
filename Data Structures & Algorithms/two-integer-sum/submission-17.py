class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Brute force: O(n^2)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
        return []
        #--------------------------------------------------
        # 2. Sorting 안해씨발

        #--------------------------------------------------
        # 4. Hash Map (One Pass): O(n)
        # Map = {}
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in Map:
        #         return [Map.get(diff), i]
        #     Map[nums[i]] = i
        #--------------------------------------------------
        
        