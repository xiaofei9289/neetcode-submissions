class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m =len(matrix)
        n = len(matrix[0])

        l = 0
        r = m*n-1

        while l <= r:
            mid = (l+r)//2
            row = mid//n
            col = mid % n
            ele = matrix[row][col]

            if ele < target:
                l = mid + 1
            elif ele > target:
                r = mid - 1
            else:
                return True
        return False