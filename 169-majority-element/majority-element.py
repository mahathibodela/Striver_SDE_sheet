class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        no = nums[0]
        c = 1
        i = 1

        while i < n:
            if nums[i] == no:
                c += 1
            else:
                c -= 1
                if c == 0:
                    no = nums[i]
                    c = 1
            i += 1
        
        c = 0
        for num in nums:
            if num == no:
                c += 1
        
        if c > (n/2):
            return no
        
        return -1
