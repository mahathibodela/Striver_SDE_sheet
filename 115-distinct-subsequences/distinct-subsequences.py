class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        def check(i, j, dp):
            if j == m:
                return 1
            if i >= n:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            tar = n - (m - (j)) + 1
            ans = 0
            for k in range(i, tar):
                if s[k] == t[j]:
                    ans += check(k + 1, j + 1, dp)
 
            dp[(i, j)] = ans
            return ans
            
        dp = {}
        n = len(s)
        m = len(t)
        k = check(0, 0, dp)
        return k