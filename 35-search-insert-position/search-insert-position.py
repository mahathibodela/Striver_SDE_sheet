class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
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
            
            return h + 1
        
        
        n = len(nums)
        return floor()
        # k = ceil()
        # if k >= 0 and nums[k - 1] == target:
        #     return k  - 1
        
        # return k

