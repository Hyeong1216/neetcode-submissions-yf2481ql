class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # two pass: detect 0s, save the location to the list, flip to 0s
        rows, cols = len(matrix), len(matrix[0])
        row_set = set()
        col_set = set()
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)
        
        for row in row_set:
            for col in range(cols):
                matrix[row][col] = 0
        
        for col in col_set:
            for row in range(rows):
                matrix[row][col] = 0
                    
        