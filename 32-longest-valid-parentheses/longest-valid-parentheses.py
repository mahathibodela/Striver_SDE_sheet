class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stack = [-1]
        res = 0
    
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack[-1] != -1 and s[stack[-1]] == '(':
                    stack.pop(-1)
                    res = max(res, i - (stack[-1]))
                else:
                    stack.append(i)
        
        return res