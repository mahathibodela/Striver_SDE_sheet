class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        

        no = ""
        s = s.lstrip()
        sign = True
        i = 0
        print(s)
        if len(s) == 0:
            return 0
        if s[0] == '-':
            i += 1
            sign = False
        elif s[0] == '+':
            i += 1
        
        maxi = str(2 ** 31 - 1)
        mini = str(2 ** 31)
        n = len(s)
        while i < n:
            if not (ord('0') <= ord(s[i]) <= ord('9')):
                break
            if len(no) == 0 and s[i] == '0':
                i += 1
                continue
            no = no + s[i]
            if sign and ((len(no) == len(maxi) and no >= maxi) or len(no) > len(maxi)):
                return 2 ** 31 - 1
            if not sign and ((len(no) == len(mini) and no >= mini) or len(no) > len(mini)):
                return -(2 ** 31)
            i += 1
        
        ans = 0
        for c in no:
            ind = ord(c) - ord('0')
            ans = ans * 10 + ind
        
        return ans if sign else -ans

        
            