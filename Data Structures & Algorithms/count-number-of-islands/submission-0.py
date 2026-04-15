class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def bfs(row, col):
            q = collections.deque()
            visit.add((row, col))
            q.append((row, col))
            while q:
                r, c = q.popleft()
                directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
                for rdir, cdir in directions:
                    newRow = r + rdir
                    newCol = c + cdir
                    if (newRow in range(rows) and
                        newCol in range(cols) and
                        grid[newRow][newCol] == "1" and
                        (newRow, newCol) not in visit):
                        q.append((newRow, newCol))
                        visit.add((newRow, newCol))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visit:
                    bfs(row, col)
                    islands += 1
        return islands