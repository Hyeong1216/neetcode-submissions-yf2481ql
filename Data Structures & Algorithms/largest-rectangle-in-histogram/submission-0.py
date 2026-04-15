class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            # while current bar is shorter than bar at top of stack
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]

                # Width calculation:
                # Right boundary: current index i
                # left boundary: previous element in stack (or -1 if stack empty)
                w = i if not stack else i - stack[-1] - 1

                max_area = max(max_area, h*w)
            stack.append(i)
        
        while stack:
            h = heights[stack.pop()]
            w = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, h*w)



        return max_area