class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def isOkay(k, i, j):
            for l in range(9):
                if board[i][l] == k:
                    return False
                
                if board[l][j] == k:
                    return False
                
                if board[3 * (i//3) + l // 3 ][3 * (j // 3) + l % 3] == k:
                    return False

            return True

        def check(board):

            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in range(ord('1'), ord('9') + 1):
                            if isOkay(chr(k), i, j):
                                board[i][j] = chr(k)
                                if check(board):
                                    return True
                                board[i][j] = '.'
                        return False
            
            return True

        check(board)