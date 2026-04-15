class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 1. BFS - multi source
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        q = collections.deque()

        # Step 1: Add all border 'O's to the queue and mark them
        #top
        for i in range(cols):
            if board[0][i] == "O":
                q.append((0, i))
                board[0][i] = "#"
        #left
        for i in range(rows):
            if board[i][0] == "O":
                q.append((i, 0))
                board[i][0] = "#"
        #right
        for i in range(rows):
            if board[i][cols-1] == "O":
                q.append((i, cols-1))
                board[i][cols-1] = "#"
        #bottom
        for i in range(cols):
            if board[rows-1][i] == "O":
                q.append((rows-1, i))
                board[rows-1][i] = "#"

        # Step 2: Multi-Source BFS
        while q:
            curr_row, curr_col = q.popleft()

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for row_dir, col_dir in directions:
                new_row = curr_row + row_dir
                new_col = curr_col + col_dir

                if new_row >= 0 and new_row < rows and \
                new_col >= 0 and new_col < cols and \
                board[new_row][new_col] == "O":
                    q.append((new_row, new_col))
                    board[new_row][new_col] = "#"

        # Step 3: final clean up
        # convert remaining O's to Xs and # back to Os
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "#":
                    board[row][col] = "O"

        #-------------------------------------------------
        # DFS
        # rows, cols = len(board), len(board[0])
        # O_marking = set()
        # for i in range()


        # def dfs(row, col):
