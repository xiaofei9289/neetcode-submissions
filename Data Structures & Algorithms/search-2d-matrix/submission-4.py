class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        length = row * col

        l = 0
        r = length - 1

        while l <= r:
            mid = (l+r)//2
            
            x_coordinate = mid // col
            y_coordinate = mid % col

            cur_val = matrix[x_coordinate][y_coordinate]

            if cur_val < target:
                l = mid + 1
            elif cur_val > target:
                r = mid - 1
            else:
                return True
        return False
            