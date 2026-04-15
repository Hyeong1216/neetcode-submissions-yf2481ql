class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        row, col = len(matrix), len(matrix[0])
        top, bottom = 0, row - 1
        left, right = 0, col - 1
        result = []

        while top <= bottom and left <= right:
            # 1. move RIGHT along the top boundary
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # 2. move DOWN along the right boundary
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            # 3. move LEFT along the bottom boundary (if still valid)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # 4. Move UP along the left boundary (if still valid)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

            





        return result
        