class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        stack = []
        n = len(nums)
        ans = [-1 for i in range(n)]

        for i in range(2* n):
            ind = i % n

            while stack and nums[stack[-1]] < nums[ind]:
                j = stack.pop(-1)
                if ans[j] == -1: ans[j] = nums[ind]
            stack.append(ind)

        return ans