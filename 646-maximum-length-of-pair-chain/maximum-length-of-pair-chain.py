class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """

        pairs.sort()
        n = len(pairs)
        dp = [1 for i in range(n)]
        ans = 1
        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
            ans = max(ans, dp[i])
        
        return ans

        