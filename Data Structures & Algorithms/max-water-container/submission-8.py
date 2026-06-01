class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Questions 
        # 1. Can the array be empty or have less than 2 elements?
        # 2. Can heights ne negative?

        # solution
        l, r = 0, len(heights) - 1
        maxArea = 0
        while l < r:
            curr_area = min(heights[l], heights[r]) * (r-l)
            maxArea = max(maxArea, curr_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1


        return maxArea

        # BigO -> O(N)












        l, r = 0, len(heights) - 1
        area = 0

        while l < r:
            currArea = (r-l) * min(heights[l], heights[r])
            area = max(area, currArea)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return area