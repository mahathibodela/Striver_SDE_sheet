class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        dp = [1 for i in range(n)]
        count = [1 for i in range(n)]
        maxi = 1
        maxiInd = -1

        for i in range(1, n):
            k = 1
            c = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > k:
                        k = dp[j] + 1
                        c = count[j]
                    elif dp[j] + 1 == k:
                        c += count[j]
            
            count[i] = c
            dp[i] = k
            if k > maxi:
                maxi = k
                maxiInd = i
        
        ans = 0
        for i in range(len(nums)):
            if dp[i] == maxi:
                ans += count[i]
        
        return ans




        