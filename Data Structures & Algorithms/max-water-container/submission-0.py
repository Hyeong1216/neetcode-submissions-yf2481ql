class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # use two-pointers > l,r > calculate and update max area

        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            tempArea = (r-l) * min(heights[l], heights[r])
            area = max(area, tempArea)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1
        return area