class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_HS=collections.defaultdict(set)
        col_HS=collections.defaultdict(set)
        square_HS=collections.defaultdict(set)
        for r in range(9):
            for c in range (9):
                if (board[r][c] =='.'):
                   continue 
                if(board[r][c] in row_HS[r] or board[r][c] in col_HS[c] or board[r][c] in square_HS[(r//3,c//3)]):
                   return False
                row_HS[r].add(board[r][c])
                col_HS[c].add(board[r][c])
                square_HS[(r//3,c//3)].add(board[r][c])
        return True 
