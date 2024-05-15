class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        ws = n - k # window with least sum
        ans = sum(cardPoints[:ws])
        tot = ans
        l = 0

        for i in range(ws, n):
            tot = tot - cardPoints[l] + cardPoints[i]
            l += 1
            ans = min(ans, tot)
       
        return sum(cardPoints) - ans



            

            
