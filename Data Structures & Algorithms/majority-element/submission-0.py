class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashmap
        count = defaultdict(int)
        n = len(nums)
        for num in nums:
            count[num] = count[num] + 1
            print(count)
            if count[num] > (n // 2):
                return num
            
