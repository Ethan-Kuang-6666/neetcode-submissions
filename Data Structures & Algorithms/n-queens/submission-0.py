class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos = set()
        neg = set()

        res = []
        board = [["."] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if c not in cols and r + c not in pos and r - c not in neg:
                    cols.add(c)
                    pos.add(r + c)
                    neg.add(r - c)
                    board[r][c] = "Q"
                    dfs(r + 1)
                    board[r][c] = "."
                    cols.remove(c)
                    pos.remove(r + c)
                    neg.remove(r - c)

            return

        dfs(0)
        return res

