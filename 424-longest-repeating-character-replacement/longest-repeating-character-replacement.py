class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """


        freq = [0 for i in range(26)]
        l = 0
        ans = 0

        for i in range(len(s)):
            c = s[i]
            freq[ord(c) - ord('A')] += 1

            while l <= i and (i - l + 1) - max(freq) > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            ans = max(ans, i - l + 1)
        
        return ans