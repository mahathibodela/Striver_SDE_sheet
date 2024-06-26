class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        

        b = -1
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                b = i
                break
    
        if b == -1:
            return nums.reverse()
        
        maxi = 10 ** 10
        maxiid = -1
        for i in range(b + 1, n):
            if nums[i] > nums[b] and nums[i] < maxi:
                maxi = nums[i]
                maxiid = i
        
        nums[b], nums[maxiid] = nums[maxiid], nums[b]
        temp = nums[b + 1:]
        temp.sort()
        i = b + 1
        for no in temp:
            nums[i] = no
            i += 1
        return nums