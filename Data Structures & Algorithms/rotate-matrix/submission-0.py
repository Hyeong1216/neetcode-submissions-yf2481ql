class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n // 2):
            cycles = n - 2 * i - 1
            
            for offset in range(cycles):
                top = (i, i + offset)
                right = (i + offset, n - i - 1)
                bottom = (n - i - 1, n - i - 1 - offset)
                left = (n - i - 1 - offset, i)

                # Extract values
                top_val = matrix[top[0]][top[1]]
                right_val = matrix[right[0]][right[1]]
                bottom_val = matrix[bottom[0]][bottom[1]]
                left_val = matrix[left[0]][left[1]]
                
                # Rotate: top → right → bottom → left → top
                matrix[right[0]][right[1]] = top_val
                matrix[bottom[0]][bottom[1]] = right_val
                matrix[left[0]][left[1]] = bottom_val
                matrix[top[0]][top[1]] = left_val
