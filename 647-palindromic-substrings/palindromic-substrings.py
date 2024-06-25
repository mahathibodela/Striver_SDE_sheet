class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        res = 0

        for i in range(n):
            l = i 
            r = i
            while l >= 0 and  r < n and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1

            l = i
            r = i + 1
            while l >= 0 and  r < n and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        
        return res


            


        