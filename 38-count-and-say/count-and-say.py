class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n == 1:
            return "1"

        def check(no, s):
            if no == n:
                return s
            
            c = 1
            ch = s[0]
            ans = ""
            for i in range(1, len(s)):
                if ch == s[i]:
                    c += 1
                else:
                    ans += str(c) + ch
                    c = 1 
                    ch = s[i]
            
            ans += str(c) + ch         
            return check(no + 1, ans)

        return check(1, "1")
        