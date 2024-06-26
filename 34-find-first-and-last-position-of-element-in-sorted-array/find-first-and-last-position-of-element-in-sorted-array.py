class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def floor():
            l = 0
            h = n - 1
            ans = -1

            while l <= h:
                mid = (l + h) / 2

                if nums[mid] < target:
                    l = mid + 1
                else:
                    h = mid - 1
            
            return h
        
        
        def ceil():
            l = 0
            h = n - 1

            while l <= h:
                mid = (l + h) / 2

                if nums[mid] <= target:
                    l = mid + 1
                else:
                    h = mid - 1
            
            return l




        n = len(nums)
        l = floor()
        h = ceil()
        if l + 1 < n and nums[l + 1] == target:
            l += 1
        else:
            l = -1
            
        if h - 1>= 0 and nums[h - 1] == target:
            h -= 1
        else:
            h = -1

        return [l, h]
        