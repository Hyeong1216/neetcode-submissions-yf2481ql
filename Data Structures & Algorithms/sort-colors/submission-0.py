class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0] * 3
        for i in range(len(nums)):
            temp[nums[i]] += 1
        
        ptr = 0  
        for i in range(len(temp)):     
            curr_range = temp[i]
            for j in range(ptr, curr_range + ptr):
                nums[j] = i
            ptr = curr_range + ptr