class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        n = len(s)
        size = numRows + numRows - 2
        r = numRows
        c = (n / size) * (1 + numRows - 2)
        rem = n % size
        if rem <= numRows:
            c += 1
        else:
            c += 1 + rem - numRows
        
        if c == 1: return s
        dp = [['#'for j in range(c)] for i in range(r)]
        i = 0
        nr = nc = 0
        down = True

        while i < n:
            if i == n - 1:
                dp[nr][nc] = s[i]
                break
            if down:
                while i < n and nr < r - 1 and nc < c:
                    dp[nr][nc] = s[i]
                    i += 1
                    nr += 1
            else:
                while i < n and nr > 0 and nc < c - 1:
                    dp[nr][nc] = s[i]
                    nr -= 1
                    nc += 1
                    i += 1


            down = not down
        print(len(s), r, c)
        
        ans = ""
        for i in range(r):
            for j in range(c):
                if dp[i][j] != '#':
                    ans += dp[i][j]
        
        return ans



                
                



        