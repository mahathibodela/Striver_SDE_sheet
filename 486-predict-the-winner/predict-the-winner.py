class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def check(i, j, p, dp):
            if i > j:
                return 0

            if (i, j, p) in dp:
                return dp[(i, j, p)]
            
            one = p * nums[i] + check(i + 1, j, -p, dp)
            two = p * nums[j] + check(i, j - 1, -p, dp)

            if p == 1:
                ans = max(one, two)
            else:
                ans = min(one, two)
            
            dp[(i, j, p)] = ans
            return ans

    
        dp = {}
        n = len(nums)
        k = check(0, n - 1, 1, dp)
        if k >= 0:
            return True
        return False