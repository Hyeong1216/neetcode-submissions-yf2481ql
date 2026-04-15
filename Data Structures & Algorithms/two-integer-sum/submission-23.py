class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #1. Brute force O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # 2. Hashmap one pass O(n)
        Map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in Map:
                # return [i, Map.get(diff)]
                return [Map.get(diff), i]

            Map[nums[i]] = i
        # return []

