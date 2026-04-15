class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float('-inf')

        # Generate all possible subarrays
        for i in range(len(nums)):          # starting position
            for j in range(i, len(nums)):   # ending position
                #calculate product of subarray from i to j
                product = 1
                for k in range(i, j+1):
                    product *= nums[k]
                max_product = max(max_product, product)
        return max_product
