class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Questions
        # 1. Can the array have duplicate values?
        # 2. Is there always exacrlt one solution?
        # 3. Can I use the same element twice?
        # 4. Should I return indices or values?
        # 5. is the array sorted?

        # Solutions
        #1. Brute force O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         temp = nums[i] + nums[j]
        #         if temp == target:
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

