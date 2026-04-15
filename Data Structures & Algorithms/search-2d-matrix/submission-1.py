class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force
        # rows, cols = len(matrix), len(matrix[0])
        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j] == target:
        #             return True
        # return False
        #-----------------------------------
        # Binary search
        rows, cols = len(matrix), len(matrix[0])
        
        #find the row
        top, bottom = 0, rows - 1
        while top <= bottom:
            mid = top + (bottom - top) // 2

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][cols-1]:
                top = mid + 1
            else:
                target_row = mid
                break
                
        else:
            return False

        # print(target_row)

        #binary search for the value
        l, r = 0, cols - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target < matrix[target_row][mid]:
                r = mid - 1
            elif matrix[target_row][mid] < target:
                l = mid + 1
            else:
                return True

        return False
 










