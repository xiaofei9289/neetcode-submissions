class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        lef = 0 
        rig = rows * cols - 1

        while lef <= rig:
            mid = (lef + rig) // 2

            x_coor = mid // cols
            y_coor = mid % cols

            val = matrix[x_coor][y_coor]

            if val < target:
                lef = mid + 1
            elif val > target:
                rig = mid - 1
            else:
                return True
        return False