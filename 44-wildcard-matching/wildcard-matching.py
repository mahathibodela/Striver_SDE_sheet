class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def check(i, j, dp):
            if i == n and j == m:
                return True
            if i == n:
                for k in range(j, m):
                    if p[k] != '*':
                        return False
                
                return True   
            if j == m:
                return False
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if p[j] == '?':
                k = check(i + 1, j + 1, dp)
            elif p[j] == '*':
                k = False
                for l in range(i, n + 1):
                    if check(l, j + 1, dp):
                        k = True
                        break
            else:
                if p[j] == s[i]:
                    k = check(i + 1, j + 1 ,dp)
                else:
                    k = False
            
            dp[(i, j)] = k
            return k

        n = len(s)
        m = len(p)
        dp = {}
        k = check(0, 0, dp)
        return k
        