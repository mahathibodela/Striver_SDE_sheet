class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rowans = colans = -1

        l = 0
        h = len(matrix) - 1
        n = h
        m = len(matrix[0]) - 1

        while(l <= h):
            mid = (l + h) // 2

            if(matrix[mid][m] >= target):
                rowans = mid
                h = mid - 1
            else:
                l = mid + 1
        
        l = 0
        h = m 
        print(rowans)
        while(l<=h):
            mid = (l + h) // 2
            print(mid)

            if(matrix[rowans][mid] == target):
                return True
            if(matrix[rowans][mid] < target):
                l= mid + 1
            else:
                h = mid - 1
        
        return False
        