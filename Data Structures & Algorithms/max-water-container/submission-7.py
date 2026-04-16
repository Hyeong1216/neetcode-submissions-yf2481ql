class Solution:
    def maxArea(self, heights: List[int]) -> int:
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