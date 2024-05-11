class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums) - 1
        nums.sort()
        if nums[h] < target :
            return h + 1
        if target < nums[0]:
            return 0

        while(l <= h):
            mid = (l + h) / 2

            if(nums[mid] < target and nums[mid + 1] > target):
                return mid + 1
            elif(nums[mid] == target):
                return mid
            
            elif(nums[mid + 1] <= target):
                l = mid + 1
            else:
                h = mid - 1
        
        return -1
        
            
        