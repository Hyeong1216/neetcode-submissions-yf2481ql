class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set() #occupied columns
        diag1 = set() #occupied diagonals (row - col)
        diag2 = set() #occupied diagonals (row + col)

        def is_safe(row, col):
            return (col not in cols) and ((row-col) not in diag1) and ((row+col) not in diag2)
        res = []
        def bt(row, curr_board):
            if row == n:
                temp_list = []
                for i in range(len(curr_board)):
                    temp_str = ""
                    for j in range(n):
                        if j == curr_board[i]:
                            temp_str += "Q"
                        else:
                            temp_str += "."
                    temp_list.append(temp_str)
                res.append(temp_list)
                return

            for col in range(n):
                if is_safe(row, col):
                    # place queen
                    curr_board.append(col)
                    cols.add(col)
                    diag1.add(row-col)
                    diag2.add(row+col)
                    # Recurse to next row
                    bt(row+1, curr_board)

                    # Backtrack (remove queen)
                    curr_board.pop()
                    cols.remove(col)
                    diag1.remove(row-col)
                    diag2.remove(row+col)

                
        
        bt(0, [])
        return res