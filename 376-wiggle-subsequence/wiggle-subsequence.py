class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        dp = [[1 for i in range(2)] for i in range(n)]
        ans = 1

        for i in range(1, n):
            for k in range(2):
    
                for j in range(i):
                    if k == 0:
                        if nums[j] < nums[i] and dp[j][1] + 1 > dp[i][0]:
                            dp[i][0] = dp[j][1] + 1
                    elif k == 1:
                        if nums[j] > nums[i] and dp[j][0] + 1 > dp[i][1]:
                            dp[i][1] = dp[j][0] + 1
                
                ans = max(ans, dp[i][k])
        
        return ans




