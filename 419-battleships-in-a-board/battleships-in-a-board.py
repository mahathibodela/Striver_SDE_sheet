class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        vis = set()
        n = len(board)
        m = len(board[0])
        ans = 0

        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    continue

                if i == 0 and j == 0:
                    ans += 1
                elif i == 0 and board[i][j - 1] != 'X':
                    ans += 1
                elif j == 0 and board[i - 1][j] != 'X':
                    ans += 1
                elif board[i-1][j] != 'X' and board[i][j - 1] != 'X':
                    ans += 1
        
        return ans
                





        