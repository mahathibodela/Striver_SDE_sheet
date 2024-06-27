class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        n = len(heights)
        leftSmall = [-1 for i in range(n)]
        rightSmall = [n for i in range(n)]

        # leftSmall
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop(-1)
            
            if stack:
                leftSmall[i] = stack[-1]
            stack.append(i)
        
        #rightSmall
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop(-1)
            
            if stack:
                rightSmall[i] = stack[-1]
            stack.append(i)
        
        ans = 0
        for i in range(n):
            ans = max(ans, heights[i] * (rightSmall[i] - leftSmall[i] - 1))
        
        return ans
            
