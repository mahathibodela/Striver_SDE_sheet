class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        dp = {}
        direct=[[-2, 1],[-1, 2],[1, 2],[2, 1],[2, -1],[1, -2],[-1, -2],[-2, -1]]


        def check(r, c, k, dp):
            if k == 0:
                return 1.0
            
            if (r, c, k) in dp:
                return dp[(r, c, k)]
            
            count = 0
            for dr, dc in direct:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    count += (check(nr, nc, k - 1, dp)) / 8
            
            dp[(r, c, k)] = count
            return count

        ans = check(row, column, k, dp)
        return ans
        