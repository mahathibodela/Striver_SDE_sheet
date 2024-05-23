class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        def check(i, j, dp):
            if i > j:
                return 0
            if i == j:
                return arr[i]
            if (i, j) in dp:
                return dp[(i, j)]
            
            ans = 0
            maxi = 0
            c = 1
            for l in range(i, min(j + 1, i + k)):
                maxi = max(maxi, arr[l])
                subans = c * maxi + check(l + 1, j, dp)
                c += 1
                ans = max(ans, subans)
            
            dp[(i, j)] = ans
            return ans

        n = len(arr)
        dp = {}
        k = check(0, n - 1, dp)
        return k
        