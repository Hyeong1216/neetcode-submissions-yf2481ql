class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1. BRUTE FORCE O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True

        # return False

        # 2. sorting O(nlogn) + O(n) -> O(nlogn)
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True

        # return False

        # 3. Hash Set (n)
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                return True
            visited.add(nums[i])
        return False