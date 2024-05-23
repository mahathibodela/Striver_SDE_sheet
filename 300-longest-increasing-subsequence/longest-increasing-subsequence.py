class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def check(ind, pre, dp):
            if ind >= n:
                return 0

            if (ind, pre) in dp:
                return dp[(ind, pre)]
  
            take = 0
            if pre == -1 or nums[ind] > nums[pre]:
                take = 1 + check(ind + 1, ind, dp)
            not_take = check(ind + 1, pre, dp)

            k = max(take, not_take)
            dp[(ind, pre)] = k
            return k

        n = len(nums)
        dp = {}
        # k = check(0, -1, dp)/

        ans = [1 for i in range(n)]
        k = 1

        for i in range(1, n):
            tot = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    tot = max(tot, ans[j] + 1)
            ans[i] = tot
            k = max(k, ans[i])
        print(ans)
        return k
        