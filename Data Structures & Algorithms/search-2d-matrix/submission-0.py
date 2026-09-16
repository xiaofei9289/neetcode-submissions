import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                temp.append(matrix[i][j])
        index = bisect.bisect_left(temp,target)
        return True if index < len(temp) and temp[index]==target else False