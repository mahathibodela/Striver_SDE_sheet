class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])

        t, b = 0, n - 1
        while t <= b:
            mid = (t + b) / 2
            if matrix[mid][0] > target:
                b = mid - 1
            else:
                t = mid + 1
        row = b
        
        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) / 2

            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False