class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        

        cur = 1
        pre = 0
        ans = 0
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                ans += min(cur, pre)
                pre = cur
                cur = 1
        
        ans += min(cur, pre)
        return ans