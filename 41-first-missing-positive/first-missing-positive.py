class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
     
        for i in range(n):
            if 1 <= abs(nums[i]) <= n:
                val = abs(nums[i])

                if nums[val - 1] < 0:
                    continue
                else:
                    nums[val - 1] = -nums[val - 1]
        
        for i in range(1, n + 1):
            if nums[i - 1] > 0:
                return i 
        return n + 1
            

