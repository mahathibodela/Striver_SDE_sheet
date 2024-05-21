class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        def check(i, n, s, dp):
            if i >= n:
                return 0
            if i == n - 1:
                if s == 0:
                    return nums[i]
                else:
                    return 0
            if (i, s) in dp:
                return dp[(i, s)]
  
            #pick
            if i == 0:
                pick = nums[i] + check(i + 2, n, 1, dp)
            else:
                pick = nums[i] + check(i + 2, n, s, dp)
            
            #unpick
            if i == 0:
                unpick = check(i + 1, n, 0, dp)
            else:
                unpick = check(i + 1, n, s, dp)
            
            ans = max(pick, unpick)
            dp[(i, s)] = ans 
            return ans
        
        # dp = {}
        # return check(0, n, 0, dp)
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        dp = [[0 for i in range(n)] for i in range(2)]
        # first choice - take i
        dp[0][n - 2] = nums[n - 2]
        for i in range(n - 3, -1, -1):
            for j in range(2):
                if j == 0:
                    dp[j][i] = max(nums[i] + dp[1][i + 1], dp[0][i + 1])
                else:
                    dp[j][i] = dp[0][i + 1]
        
        dp2 = [[0 for i in range(n)] for i in range(2)]
        # first choice - take i
        dp2[0][n - 1] = nums[n - 1]
        for i in range(n - 2, 0, -1):
            for j in range(2):
                if j == 0:
                    dp2[j][i] = max(nums[i] + dp2[1][i + 1], dp2[0][i + 1])
                else:
                    dp2[j][i] = dp2[0][i + 1]
      
        return max(dp[0][0], dp2[0][1])

        
