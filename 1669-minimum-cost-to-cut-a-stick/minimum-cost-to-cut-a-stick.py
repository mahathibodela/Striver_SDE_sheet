class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """

        def check(l, h, ss, se, dp):
            if l > h:
                return 0
            
            if (l, h) in dp:
                return dp[(l, h)]
            
            ans = 10 ** 10
            for i in range(l, h + 1):
                cut = cuts[i]
                k = se - ss + check(l, i - 1, ss, cut, dp) + check(i + 1, h, cut, se, dp)
                ans = min(ans, k)
            
            dp[(l, h)] = ans
            return ans

        h = len(cuts)
        dp = {}
        cuts.sort()
        k = check(0, h - 1, 0, n, dp)
        return k
        
        