class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """

        def check(ind, nums):
            if ind == n + 1:
                return 1
            
            count = 0
            for i in range(ind, n + 1):
                if nums[i] % ind == 0 or ind % nums[i] == 0:
                    nums[i], nums[ind] = nums[ind], nums[i]
                    count += check(ind + 1, nums)
                    nums[i], nums[ind] = nums[ind], nums[i]
                
            return count
        
        nums = [i for i in range(n + 1)]
        k = check(1, nums)
        return k