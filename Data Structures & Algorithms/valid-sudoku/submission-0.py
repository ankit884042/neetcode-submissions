class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            for j in range(9):

                if board[i][j] == ".":
                    continue

                num = board[i][j]

                # Check row
                for k in range(9):
                    if k != j and board[i][k] == num:
                        return False

                # Check column
                for k in range(9):
                    if k != i and board[k][j] == num:
                        return False

                # Find starting position of 3x3 box
                start_row = (i // 3) * 3
                start_col = (j // 3) * 3

                # Check 3x3 box
                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):
                        if (r != i or c != j) and board[r][c] == num:
                            return False

        return True