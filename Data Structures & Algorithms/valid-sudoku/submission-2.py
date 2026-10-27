class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 第一步：检查每一行
        for r in range(9):
            seen = set()

            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                if num in seen:
                    return False

                seen.add(num)

        # 第二步：检查每一列
        for c in range(9):
            seen = set()

            for r in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                if num in seen:
                    return False

                seen.add(num)

        # 第三步：检查每个九宫格
        for start_r in range(0, 9, 3):
            for start_c in range(0, 9, 3):

                seen = set()

                for r in range(start_r, start_r + 3):
                    for c in range(start_c, start_c + 3):

                        num = board[r][c]

                        if num == ".":
                            continue

                        if num in seen:
                            return False

                        seen.add(num)

        return True