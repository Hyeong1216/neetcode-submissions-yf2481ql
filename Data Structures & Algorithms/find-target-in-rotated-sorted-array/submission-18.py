class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1


        while l <= r: #flag: not <= because we are comparing l, r value and it shouldn't be pointing to same element
            m = l + (r-l) // 2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]: # left half is sorted
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # right half is sorted
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1































# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             m = l + (r-l) // 2
#             if target == nums[m]:
#                 return m

#             # 4 possible cases
#             if nums[l] <= nums[m]: # left half is sorted
#                 if nums[l] <= target < nums[m]:
#                     r = m - 1
#                 else:
#                     l = m + 1


#             else: # right half is sorted
#                 if nums[m] < target <= nums[r]:
#                     l = m + 1
#                 else:
#                     r = m - 1

#         return -1





























# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             mid = l + (r-l) // 2
#             if target == nums[mid]:
#                 return mid

#             if nums[l] <= nums[mid]: 
#                 if target > nums[mid] or target < nums[l]: 
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#             else: 
#                 if target < nums[mid] or target > nums[r]: 
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#         return -1 