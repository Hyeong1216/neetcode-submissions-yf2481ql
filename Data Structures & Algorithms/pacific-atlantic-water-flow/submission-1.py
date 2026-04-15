class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])

        # Two sets to track wich cells can reach each ocean
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(row, col, reachable, prev_height):
            if row < 0 or row >= rows or col < 0 or col >= cols or heights[row][col] < prev_height or (row, col) in reachable:
                return
            
            reachable.add((row, col))
            dfs(row+1, col, reachable, heights[row][col])
            dfs(row-1, col, reachable, heights[row][col])
            dfs(row, col+1, reachable, heights[row][col])
            dfs(row, col-1, reachable, heights[row][col])
        
        for col in range(cols):
            dfs(0, col, pacific_reachable, float("-inf"))
        for row in range(rows):
            dfs(row, 0, pacific_reachable, float("-inf"))
        
        for col in range(cols):
            dfs(rows-1, col, atlantic_reachable, float("-inf"))
        for row in range(rows):
            dfs(row, cols-1, atlantic_reachable, float("-inf"))

        result = []

        for cell in pacific_reachable & atlantic_reachable:
            result.append(list(cell))
        return result

