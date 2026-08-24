class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # dutch flag
        def swap(i1, i2):
            temp = nums[i1]
            nums[i1] = nums[i2]
            nums[i2] = temp

        l, m, h = 0, 0, len(nums) - 1
        while m <= h:
            curr = nums[m]
            if curr == 0:
                swap(l, m)
                l += 1
                m += 1
            elif curr == 1:
                m += 1
            else:
                swap(m, h)
                h -= 1











        #-------------------------------------------------------
        # countint-sort two pass
        # temp = [0] * 3
        # for i in range(len(nums)):
        #     temp[nums[i]] += 1
        
        # ptr = 0  
        # for i in range(len(temp)):     
        #     curr_range = temp[i]
        #     for j in range(ptr, curr_range + ptr):
        #         nums[j] = i
        #     ptr = curr_range + ptr