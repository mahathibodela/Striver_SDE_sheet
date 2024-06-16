class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = []
        
        e = o = 0
        for i in range(len(nums)):
            no = nums[i]
            if i % 2 == 0:
                e += no
            else:
                o += no
            left.append((e, o))
        

        ans = 0
        n = len(nums)
        for i in range(n):
            if i == 0:
                nes = left[n - 1][1] - left[0][1]
                nos = left[n - 1][0] - left[0][0]
            else:
                nes = left[i - 1][0] + left[n - 1][1] - left[i][1]
                nos = left[i - 1][1] + left[n - 1][0] - left[i][0]
            
            if nes == nos:
                ans += 1
        
        return ans
        
   


        