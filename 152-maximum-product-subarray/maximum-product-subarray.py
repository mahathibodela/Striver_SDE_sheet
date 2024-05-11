class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxPro = 1
        minPro = 1
        ans = max(nums)

        for no in nums:
            if no == 0:
                maxPro = 1
                minPro = 1
                continue
            
            if no > 0:
                maxPro = max(maxPro * no, no)
                minPro = min(minPro * no, no)
            
            else:
                temp = maxPro
                maxPro = max(minPro * no, no)
                minPro = min(temp * no, no)
            
            ans = max(ans, maxPro)
        
        return ans


        