class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0
        n = len(nums)

        while i < n:

            while i < n and nums[i] != val:
                i += 1

            j = i + 1
            while j < n and nums[j] == val:
                j += 1
            
            if j < n:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            else:
                break
        
        return i

        