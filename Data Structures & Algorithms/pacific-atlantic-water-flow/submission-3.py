class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # DFS
        # 1. base case: height is None
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])

        # 2. Two sets to track wich cells can reach each ocean
        pacific_reachable = set()
        atlantic_reachable = set()

        # 3. run the dfs (four parameters)
        def dfs (row, col, reachable, prev_height):
            if row < 0 or row >= rows or col < 0 or col >= cols or heights[row][col] < prev_height or (row, col) in reachable:
                return
            reachable.add((row, col))
            dfs(row+1, col, reachable, heights[row][col])
            dfs(row-1, col, reachable, heights[row][col])
            dfs(row, col+1, reachable, heights[row][col])
            dfs(row, col-1, reachable, heights[row][col])

        # 4. run four for loops for row and col of each ocean
        # Pacific: top row
        for i in range(cols):
            dfs(0, i, pacific_reachable, float('-inf'))
        # Pacific: left col
        for i in range(1, rows):
            dfs(i, 0, pacific_reachable, float('-inf'))
        # Atlantic: bottom row
        for i in range(cols):
            dfs(rows-1, i, atlantic_reachable, float('-inf'))
        # Atlantic: right col
        for i in range(rows-1):
            dfs(i, cols-1, atlantic_reachable, float('-inf'))
        
        # 5. find the intersection
        result =[]
        for cell in pacific_reachable & atlantic_reachable:
            result.append([cell[0], cell[1]])
        # 6. return
        return result
        #-------------------------------------------------------------------------------
        # BFS







        #-------------------------------------------------------------------------------
        # DFS solution
        # if not heights:
        #     return []
        # rows, cols = len(heights), len(heights[0])

        # # Two sets to track wich cells can reach each ocean
        # pacific_reachable = set()
        # atlantic_reachable = set()

        # def dfs(row, col, reachable, prev_height):
        #     if row < 0 or row >= rows or col < 0 or col >= cols or heights[row][col] < prev_height or (row, col) in reachable:
        #         return
            
        #     reachable.add((row, col))
        #     dfs(row+1, col, reachable, heights[row][col])
        #     dfs(row-1, col, reachable, heights[row][col])
        #     dfs(row, col+1, reachable, heights[row][col])
        #     dfs(row, col-1, reachable, heights[row][col])
        
        # for col in range(cols):
        #     dfs(0, col, pacific_reachable, float("-inf"))
        # for row in range(rows):
        #     dfs(row, 0, pacific_reachable, float("-inf"))
        
        # for col in range(cols):
        #     dfs(rows-1, col, atlantic_reachable, float("-inf"))
        # for row in range(rows):
        #     dfs(row, cols-1, atlantic_reachable, float("-inf"))

        # result = []

        # for cell in pacific_reachable & atlantic_reachable:
        #     result.append(list(cell))
        # return result

