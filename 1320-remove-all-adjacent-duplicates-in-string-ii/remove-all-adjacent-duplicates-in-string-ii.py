class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        stack = []

        for c in s:
            if stack:
                char, count = stack[-1]
                if c == char:
                    stack[-1][1] = count + 1
                    if count + 1 == k:
                        temp = stack.pop(-1)
                    continue
            stack.append([c, 1])
        
        ans = ""
        for c, co in stack:
            ans += c * co
        
        return ans