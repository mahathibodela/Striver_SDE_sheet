class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)

        for i in range(2 ** n):
            temp = []
            for j in range(n):
                if (i >> j) & 1 == 1:
                    temp.append(nums[j])
            ans.append(temp)
        
        return ans
