class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary Search
        # 길이가 짧은 인풋 기준으로 두개 리스트의 길이의 합산 나누기 2를 한뒤
        # 길이가 짧은 인풋의 mid포인트 위에서 나눈값에서 빼서 그 길이만큼
        # 길이가 긴 인풋을 서치하고
        # 두 인풋의 경계선에서 전체 길이를 odd/even에따라 mid point를 구한다
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total //2
        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1

        while True:
            i = l + (r - l) // 2 # A
            j = half - i - 2 # B

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: # need to reduce size of A
                r = i - 1
            else:
                l = i + 1
                





        #------------------------------------------------------------------------------
        # Merge arrays in ascending order: O(m+n)
        # res = []
        # ptr1, ptr2 = 0, 0
        # while ptr1 < len(nums1) and ptr2 < (len(nums2)):
        #     #print(f"ptr1:{ptr1} || ptr2:{ptr2}")
        #     if nums1[ptr1] <= nums2[ptr2]:
        #         res.append(nums1[ptr1])
        #         ptr1 += 1
        #     else:
        #         res.append(nums2[ptr2])
        #         ptr2 += 1              
        # while ptr1 < len(nums1):
        #     res.append(nums1[ptr1])
        #     ptr1 += 1
        # while ptr2 < len(nums2):
        #     res.append(nums2[ptr2])
        #     ptr2 += 1
        # #print(res)
        # if len(res) % 2 != 0: #odd length
        #     mid = 0 + (len(res) - 0) // 2
        #     return res[mid]
        # else: #even length
        #     mid = 0 + (len(res) - 0) // 2
        #     return (res[mid] + res[mid-1])/2
