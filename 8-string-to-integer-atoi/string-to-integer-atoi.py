class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxPos = str(2**31 - 1)
        minPos = str((2**31))
        print("5" > "332")

        #trim down all leading white spaces
        for i in range(len(s)):
            if s[i] != " ":
                s = s[i:]
                break
        
        #checking the string
        ans = ""
        for i in range(len(s)):
            if i == 0:
                if s[i] == '+':
                    continue
                elif s[i] == '-':
                    ans += s[i]
                    continue
            
            if '0' <= s[i] and s[i] <= '9':
                if((ans == "" or ans =="-" or ans =='+') and s[i] == '0'):
                    continue

                ans += s[i]
                if ans[0] == '-' and (((len(ans[1:]) == len(minPos)) and ans[1:] >= minPos) or (len(ans[1:]) > len(minPos))):
                    return -(2 ** 31)
                elif ans[0] != '-' and ((len(ans) == len(maxPos) and ans >= maxPos) or (len(ans) > len(maxPos))):
                    return (2 ** 31) - 1
                
            else:
                break
        

        if ans == "" or ans == '-':   return 0
        if ans[0] == '-':
            return -(int(ans[1:]))
        return int(ans)


        
        
        