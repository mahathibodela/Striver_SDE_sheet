class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        heap = []
        for key, item in count.items():
            heapq.heappush(heap, (-item, key))
        
        ans = ""
        prec, prevFreq = "", 0
        while len(ans) < len(s):
            if not heap:
                return ""

            curF, curc = heapq.heappop(heap)
            ans += str(curc)
            
            if prevFreq != 0:
                heapq.heappush(heap, (prevFreq, prevc))
                prevFreq = 0

            if curF != -1:
                prevFreq = curF + 1
                prevc = curc
        
        return ans

