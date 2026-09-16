class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows=len(matrix)
        columns=len(matrix[0])

        lef=0
        righ=rows*columns-1
        while lef<=righ:
            mid=lef+(righ-lef)//2
            row=mid//columns
            col=mid%columns
            if matrix[row][col]<target:
                lef=mid+1
            elif matrix[row][col]>target:
                righ=mid-1
            else:
                return True
        return False
        