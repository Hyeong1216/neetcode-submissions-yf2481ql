class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Fast and slow pointers
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(f"slow:{slow}||fast:{fast}")
            if slow == fast:
                break
        print()
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            print(f"slow:{slow}||slow2:{slow2}")

            if slow == slow2:
                return slow

        #-----------------------
        # Binary search
        # low, high = 1, len(nums) - 1

        # while low < high:
        #     mid = low + (high-low) // 2
        #     lessOrEqual = sum(1 for num in nums if num <= mid)
        #     if lessOrEqual <= mid:
        #         low = mid + 1
        #     else:
        #         high = mid
        
        # return low