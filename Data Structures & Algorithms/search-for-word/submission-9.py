class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #dfs
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col, index, visited):
            if index == len(word):
                return True
            visited.add((row, col))
            

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr, nc) not in visited and board[nr][nc] == word[index]:
                    if dfs(nr, nc, index+1, visited):
                        return True
                    
            
            visited.remove((row, col))
            return False

            

        
        

        for row in range(rows):
            for col in range(cols):
                visited = set()
                if board[row][col] == word[0]:
                    if dfs(row, col, 1, visited):
                        return True
        

        return False