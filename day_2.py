class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = []
            j = 0
            while j < 9:
                if board[i][j] != ".":
                    row.append(board[i][j])
                j += 1
            row_set = set(row)
            if len(row) != len(row_set):
                return False
            j = 0
        for k in range(9):
            col = []
            l = 0
            while l < 9:
                if board[l][k] != ".":
                    col.append(board[l][k])
                l += 1
            col_set = set(col)
            if len(col) != len(col_set):
                return False
            l = 0

        res = []
        for x in range(9):
            for y in range(9):
                if board[x][y] != '.':
                    val = (x // 3, y // 3, board[x][y])
                    if val not in res:
                        res.append(val)
                    else:
                        return False
        return True
