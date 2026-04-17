class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary Search
        rows, cols = len(matrix), len(matrix[0])

        #finding the row
        top, bottom = 0, rows - 1
        while top <= bottom:
            mid = top + (bottom - top) //2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][cols-1]:
                top = mid + 1
            else:
                target_row = mid
                break
        else:
            return False
        

        l, r = 0, cols - 1
        while l <= r:
            mid = l + (r-l) //2
            if target < matrix[target_row][mid]:
                r = mid - 1
            elif target > matrix[target_row][mid]:
                l = mid + 1
            else:
                return True
        return False




        # Brute force:
        # rows, cols = len(matrix), len(matrix[0])
        # for row in range(rows):
        #     for col in range(cols):
        #         if matrix[row][col] == target:
        #             return True
        # return False