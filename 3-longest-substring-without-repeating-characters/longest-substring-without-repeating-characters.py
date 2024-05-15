class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        index = {}
        l = 0
        ans = 0

        for i in range(len(s)):
            c = s[i]
            if c in index:
                l = max(l, index[c] + 1)
            
            ans = max(ans, i - l + 1)
            index[c] = i
            print(i, ans)
        
        return ans

        