class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 1. Brute Force: O(n^3)
        # max_product = float('-inf')

        # # Generate all possible subarrays
        # for i in range(len(nums)):          # starting position
        #     for j in range(i, len(nums)):   # ending position
        #         #calculate product of subarray from i to j
        #         product = 1
        #         for k in range(i, j+1):
        #             product *= nums[k]
        #         max_product = max(max_product, product)
        # return max_product

        # 2. Brute force O(n^2)
        max_product = float('-inf')

        # Generate all possible subarrays
        for i in range(len(nums)):          # starting position
            product = 1
            for j in range(i, len(nums)):   # ending position
                product *= nums[j]
                max_product = max(max_product, product)
        return max_product
