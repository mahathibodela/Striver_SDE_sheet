class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        up = True
        r = c = 0
        n = len(mat)
        m = len(mat[0])

        while r < n and c < m:
            if up:
                while r > 0 and c < m - 1:
                    ans.append(mat[r][c])
                    r -= 1
                    c += 1
                ans.append(mat[r][c])

                if c + 1 < m: c += 1
                else: r += 1
            
            else:
                while r < n - 1 and c > 0:
                    ans.append(mat[r][c])
                    r += 1
                    c -= 1
                ans.append(mat[r][c])

                if r + 1 < n: r += 1
                else: c += 1
            
            up = not up
        
        return ans
        

