class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # in BS what all we do is to eliminate..
        # think in which pos the given element cant lie
        m = len(matrix)
        n = len(matrix[0])

        row, col = 0, n - 1
        while(row < m and col >= 0):
            if(matrix[row][col] == target):
                return True
            
            if(matrix[row][col] < target):
                row += 1
            else:
                col -= 1
        
        return False

        
        