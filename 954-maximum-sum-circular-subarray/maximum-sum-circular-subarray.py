class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def getMax(nums):
            cur = 0
            maxi = -(10 ** 10)

            for no in nums:
                cur += no
                maxi = max(cur, max(maxi, no))

                if cur < 0:
                    cur = 0
            return maxi
        
        def getMin(nums):
            cur = 0
            mini = 10 ** 10

            for no in nums:
                cur += no
                cur = min(cur, no)
                mini = min(cur, min(mini, no))
            
            return mini

        tot = sum(nums)

        maxi = getMax(nums)
        mini = getMin(nums)
        if mini == tot:
            return maxi
        return max(maxi, tot - mini)