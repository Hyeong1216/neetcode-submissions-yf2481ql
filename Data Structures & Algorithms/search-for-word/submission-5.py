class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #dfs
        rows, cols = len(board), len(board[0])

        def dfs(row, col, position, visited):
            print(f"row:{row}||col:{col}")
            if position == len(word):
                return True
            
            visited.add((row, col))

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for rowDir, colDir in directions:
                newRow = rowDir + row
                newCol = colDir + col

                if newRow >= 0 and newRow < rows and \
                newCol >= 0 and newCol < cols and \
                board[newRow][newCol] == word[position] and (newRow, newCol) not in visited:
                    if dfs(newRow, newCol, position+1, visited):
                        return True
            visited.remove((row, col))
            return False
            
        for i in range(rows):
            for j in range(cols):
                visited = set()

                if board[i][j] == word[0]:
                    if dfs(i, j, 1, visited):
                        return True
        return False
            
