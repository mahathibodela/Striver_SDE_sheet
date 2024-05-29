class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        nt = set()
        n = len(s)

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) > 1:
                    stack.pop(-1)
                elif len(stack) == 1:
                    nt.add(i)
                    nt.add(stack[-1])
                    stack.pop(-1)
        

        ans = ""
        for i in range(n):
            if i not in nt:
                ans += s[i]
        
        return ans