class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ind = [-1, -1, -1]
        ans = 0

        for i in range(len(s)):
            c = s[i]
            ind[ord(c) - ord('a')] = i
            k = min(ind)
            if k != -1:
                ans += k + 1
        
        return ans

            
        