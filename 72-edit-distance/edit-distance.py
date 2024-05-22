class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        def check(i, j, dp):
            if i == n and j == m:
                return 0
            if i == n:
                return m - j 
            if j == m:
                return n - i
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            ans = 10 ** 10
            if word1[i] == word2[j]:
                ans = min(ans, check(i + 1, j + 1, dp))
            else:
                ans = min(ans, 1 + check(i, j + 1, dp))
                ans = min(ans, 1 + check(i + 1, j, dp))
                ans = min(ans, 1 + check(i + 1, j + 1, dp))
            
            dp[(i, j)] = ans
            return ans
            

        n = len(word1)
        m = len(word2)
        dp = {}
        k = check(0, 0, dp)
        return k