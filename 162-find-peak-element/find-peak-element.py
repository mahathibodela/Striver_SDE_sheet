class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        h = len(nums) - 1

        if(h == 0): return h
        if(nums[l] > nums[l + 1]): return l
        if(nums[h] > nums[h - 1]): return h


        ans = -(10 ** 10)
        ansid = -1
        l += 1
        h -= 1

        while(l <= h):
            mid = (l + h) / 2

            if(nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]):
                return mid

            if(nums[mid - 1] <= nums[mid]):
                l = mid + 1
            
            else:
                h = mid - 1
        
        return ansid

        