class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        has = set()
        ans = 0

        for char, freq in count.items():

            while freq > 0 and freq in has:
                freq -= 1
                ans += 1
            
            has.add(freq)
        
        return ans