class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = 0
        h = len(nums) - 1
        if h == 0 or nums[l] != nums[l + 1]:
            return nums[l]
        if nums[h] != nums[h - 1]:
            return nums[h]
        
        l += 1
        h -= 1

        while l <= h:
            mid = (l + h) / 2

            if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
                return nums[mid]
             
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 != 0 and nums[mid] == nums[mid - 1]):
                l = mid + 1
            else:
                h = mid - 1
        
        return -1