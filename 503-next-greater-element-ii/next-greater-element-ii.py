class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        nge = [-1 for i in range(n)]
        stack = []
        l = 2 * n

        for i in range(l):
            no = nums[i % n]

            while len(stack) != 0 and nums[stack[-1]] < no:
                j = stack[-1]
                nge[j] = nums[i % n]
                stack.pop(-1)

            stack.append(i % n)

        return nge

        