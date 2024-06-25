class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        
        pairs.sort(key = lambda p: p[1])
        pre = 0
        c = 1

        for i in range(1, len(pairs)):
            s, e = pairs[i]
            if pairs[pre][1] < s:
                c += 1
                pre = i
        
        return c