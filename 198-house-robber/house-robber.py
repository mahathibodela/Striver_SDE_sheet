class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        n = len(nums)
        # dp = {}
        # k = check(0, 0, dp)

        dp = [[0 for i in range(n)] for i in range(2)]
        dp[0][n-1] = nums[n-1]
        
        for i in range(n-2, -1, -1):
            for j in range(2):
                if j == 0:
                    dp[j][i] = max(nums[i] + dp[1][i + 1], dp[j][i + 1])
                else:
                    dp[j][i] = dp[0][i + 1]
        
        return dp[0][0]


        