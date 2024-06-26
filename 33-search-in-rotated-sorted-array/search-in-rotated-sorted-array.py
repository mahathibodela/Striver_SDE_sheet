class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n - 1
        if nums[0] == target: return 0
        if nums[-1] == target: return n - 1
        if r == 0: return -1

        while l <= r:
            mid = (l + r) / 2

            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[r] >= nums[mid]:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1