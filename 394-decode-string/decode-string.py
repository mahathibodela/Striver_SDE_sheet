class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        i = 0
        n = len(s)
        while i < len(s): 

            c = s[i]
            num = ""
            while i < n and ord('0') <= ord(c) <= ord('9'):
                num += c
                i += 1
                c = s[i]

            if num != "":
                stack.append(num)

            if c != ']':
                stack.append(c)
            else:
                temp = ""
                while stack[-1] != '[':
                    temp = stack[-1] + temp
                    stack.pop(-1)
                print(stack)
                stack.pop(-1)
                no = stack.pop(-1)
                temp = temp * int(no)
                stack.append(temp)
            
            i += 1
        
        ans = ""
        for c in stack:
            ans += c
        
        return ans
            
        