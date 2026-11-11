class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        n = row * col

        lef = 0 

        rig = n - 1

        while lef <= rig:
            mid = (lef + rig) // 2
            index_row = mid // col
            index_col = mid % col
            value = matrix[index_row][index_col]

            if value < target:
                lef = mid + 1
            elif value > target:
                rig = mid - 1
            else:
                return True
        return False