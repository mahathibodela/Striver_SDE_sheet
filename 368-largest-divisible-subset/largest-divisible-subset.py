class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        parent = [i for i in range(n)]
        dp = [1 for i in range(n)]
        maxi = 1
        maxiInd = -1

        for i in range(1, n):
            ans = 1
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if ans < dp[j] + 1:
                        ans = dp[j] + 1
                        parent[i] = j
            
            dp[i] = ans
            if dp[i] > maxi:
                maxi = dp[i]
                maxiInd = i
        
        if maxiInd == -1:
            return [nums[0]]
        i = maxiInd
        ans = []
        while i != parent[i]:
            ans.insert(0, nums[i])
            i = parent[i]
        ans.insert(0, nums[i])
        
        return ans



        