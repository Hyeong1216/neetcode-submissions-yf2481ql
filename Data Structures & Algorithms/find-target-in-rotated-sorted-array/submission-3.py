class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]: #check if first to mid element is sorted
                
                if target > nums[mid] or target < nums[l]: 
                # target is bigger than nums[mid], 
                # meaning it's placed in the second half of the list,
                # OR, target is less than nums[l]
                    l = mid + 1
                else:
                    r = mid - 1

            else: #when first to mid element is not sorted
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1