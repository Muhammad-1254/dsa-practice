class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(0, 9):
            # first checking row and col wise
            for j in range(0, 9):
                c_row = board[i][j]
                c_row_pos = [i, j]

                c_col = board[j][i]
                c_col_pos = [j, i]

                for k in range(0, 9):
                    if (
                        c_row.isnumeric()
                        and board[i][k].isnumeric()
                        and c_row_pos != [i, k]
                        and c_row == board[i][k]
                    ) or (
                        c_col.isnumeric()
                        and board[k][i].isnumeric()
                        and c_col_pos != [k, i]
                        and c_col == board[k][i]
                    ):
                        print(f"i:{i}, j:{j}, k:{k}")
                        return False
        # now checking grid wise
        # we alread check each item to its row and col wise, therefore we have only calculate as we find determiant of 3x3 matrix
        for i in range(9):
            start_row = (i // 3) * 3
            start_col = (i % 3) * 3
            visited  = set()
            for j in range(3):
                for k in range(3):
                    c = board[start_row + j][start_col + k]
                    if c.isnumeric() and  c in visited :
                        return False
                    visited .add(c)
        return True
