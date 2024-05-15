class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        l = 0
        ans = 0
        index = []

        for i in range(len(nums)):
            if nums[i] == 0:
                index.append(i)
                if k == 0 or len(index) == k + 1:
                    l = index[0] + 1
                    index.pop(0)
                
            
            ans = max(ans, i - l + 1)
        
        return ans



        