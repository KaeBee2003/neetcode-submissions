class Solution:
    from collections import defaultdict
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == ".":
                    continue
                elif curr in rows[i] or curr in cols[j] or curr in squares[i//3, j//3]:
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[i//3, j//3].add(board[i][j])

        return True
        