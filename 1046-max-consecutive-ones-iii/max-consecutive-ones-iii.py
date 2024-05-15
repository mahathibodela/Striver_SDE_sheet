class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        l = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1

                while count > k:
                    if nums[l] == 0:
                        count -= 1
                    l += 1
            
            ans = max(ans, i - l + 1)
        
        return ans



        