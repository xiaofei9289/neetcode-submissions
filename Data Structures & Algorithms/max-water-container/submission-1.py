class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(heights) - 1
        res = []

        while left_pointer < right_pointer:
            height = min(
                heights[left_pointer],
                heights[right_pointer]
            )
            colume = height * (right_pointer - left_pointer)
            res.append(colume)

            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max(res)
