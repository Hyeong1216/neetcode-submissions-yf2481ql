class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(1) space solution
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][col] == 0 for col in range(cols))
        first_col_zero = any(matrix[row][0] == 0 for row in range(rows))

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        for row in range(1, rows):
            if matrix[row][0] == 0:
                for col in range(cols):
                    matrix[row][col] = 0
        for col in range(1, cols):
            if matrix[0][col] == 0:
                for row in range(rows):
                    matrix[row][col] = 0
        if first_row_zero:
            for col in range(cols):
                matrix[0][col] = 0
        if first_col_zero:
            for row in range(rows):
                matrix[row][0] = 0
        #----------------------------------------------------------------
        # two pass: detect 0s, save the location to the list, flip to 0s
        # not O(1) space
        # rows, cols = len(matrix), len(matrix[0])
        # row_set = set()
        # col_set = set()
        # for row in range(rows):
        #     for col in range(cols):
        #         if matrix[row][col] == 0:
        #             row_set.add(row)
        #             col_set.add(col)
        
        # for row in row_set:
        #     for col in range(cols):
        #         matrix[row][col] = 0
        
        # for col in col_set:
        #     for row in range(rows):
        #         matrix[row][col] = 0
                    
        