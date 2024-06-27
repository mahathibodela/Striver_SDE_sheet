class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        n = len(matrix)
        m = len(matrix[0])
        ans = []

        l = t = 0
        r = m - 1
        b = n - 1

        while l < r and t < b:

            # topLeft to topRight
            for i in range(0, r - l):
                ans.append(matrix[t][l + i])

            #topRight to bottomRight
            for i in range(0, b - t):
                ans.append(matrix[t + i][r])
            
            #bottomRight to bottomLeft
            for i in range(0, r - l):
                ans.append(matrix[b][r - i])
            
            #bottomLeft to bottomTop
            for i in range(0, b - t):
                ans.append(matrix[b - i][l])
            
            l += 1
            r -= 1
            t += 1
            b -= 1
        
        if l == r:
            for i in range(0, b - t + 1):
                ans.append(matrix[t + i][l])
        if t == b and l != r:
            for i in range(0, r - l + 1):
                ans.append(matrix[t][l + i])
        
        return ans



