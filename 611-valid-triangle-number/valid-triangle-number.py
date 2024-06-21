class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = len(nums) - 1 
        count = 0

        while i >= 2:
            l = 0
            h = i - 1

            while l < h:
                if nums[l] + nums[h] > nums[i]:
                    count += h - l
                    h -= 1
                else:
                    l += 1
            i -= 1
        
        return count
        