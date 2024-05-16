class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        arr = heights
        n = len(arr)
        nums = arr
        rightSmall = [n for i in range(n)]
        leftSmall = [-1 for i in range(n)]
        stack = []

        for i in range(n):
            no = arr[i]
            while len(stack) != 0 and nums[stack[-1]] > no:
                j = stack[-1]
                rightSmall[j] = i
                stack.pop(-1)
            stack.append(i)
        
        stack = []
        for i in range(n -1, -1, -1):
            no = arr[i]
            while len(stack) != 0 and nums[stack[-1]] > no:
                j = stack[-1]
                leftSmall[j] = i
                stack.pop(-1)
            stack.append(i) 
        
        # print(leftS)
        ans = 0
        for i in range(n):
            l = leftSmall[i] + 1
            r = rightSmall[i] - 1
            ans = max(ans, (r - l + 1) * nums[i])
        
        return ans
        