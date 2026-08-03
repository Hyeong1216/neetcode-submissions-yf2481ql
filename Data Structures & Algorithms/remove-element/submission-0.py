class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # in-place changing the order on the go, we should not use for-loop
        # certain # iterations, instead using while

        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1


        return n