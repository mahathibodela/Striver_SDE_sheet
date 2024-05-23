class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for i in range(m)] for j in range(n)]
        ans = 0

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    if matrix[i][j] == 1:
                        up = dp[i - 1][j]
                        left = dp[i][j - 1]
                        dia = dp[i- 1][j - 1]
                        dp[i][j] = min(up, min(left, dia)) + 1
                ans += dp[i][j]
        
        return ans

                
        