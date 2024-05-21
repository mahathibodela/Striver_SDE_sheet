class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m - 1 and j == n - 1 and obstacleGrid[i][j] == 0:
                    dp[i][j] = 1
                elif i == m - 1 and obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i][j + 1]
                elif j == n - 1 and obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i + 1][j]
                elif obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        
        return dp[0][0]
        