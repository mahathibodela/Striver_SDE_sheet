class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        freq = {}
        ans = 0

        for no in time:
            rem = no % 60
            another = (60 - rem) % 60

            if another in freq:
                ans += freq[another]
            
            if rem in freq:
                freq[rem] += 1
            else:
                freq[rem] = 1
        
        return ans
