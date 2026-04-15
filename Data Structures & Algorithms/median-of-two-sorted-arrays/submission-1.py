class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge arrays in ascending order: O(m+n)
        res = []
        ptr1, ptr2 = 0, 0
        while ptr1 < len(nums1) and ptr2 < (len(nums2)):
            #print(f"ptr1:{ptr1} || ptr2:{ptr2}")
            if nums1[ptr1] <= nums2[ptr2]:
                res.append(nums1[ptr1])
                ptr1 += 1
            else:
                res.append(nums2[ptr2])
                ptr2 += 1              
        while ptr1 < len(nums1):
            res.append(nums1[ptr1])
            ptr1 += 1
        while ptr2 < len(nums2):
            res.append(nums2[ptr2])
            ptr2 += 1
        #print(res)
        if len(res) % 2 != 0: #odd length
            mid = 0 + (len(res) - 0) // 2
            return res[mid]
        else: #even length
            mid = 0 + (len(res) - 0) // 2
            return (res[mid] + res[mid-1])/2


        # Binary Search