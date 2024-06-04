class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        def check(i, dp):
            if i in dp:
                return dp[i]
            
            count = 1
            for j in range(i - 1, -1, -1):
                if arr[i] % arr[j] == 0 and arr[i] / arr[j] in has:
                    lc = check(j, dp)
                    rc = check(noToind[arr[i] / arr[j]], dp)
                    count += (lc * rc) % mod
                    count = count % mod

            dp[i] = count
            
            return count
                    
        
        mod = 10 ** 9 + 7
        n = len(arr)
        arr.sort()
        has = set()
        noToind = {}
        for i in range(n):
            has.add(arr[i])
            noToind[arr[i]] = i
        
        dp = {}
        ans = 0
        for i in range(n - 1, -1, -1):
            ans += check(i, dp) % mod
            ans = ans % mod

        return ans