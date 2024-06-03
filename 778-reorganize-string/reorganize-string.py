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
        for a, b in count.items():
            heap.append((-b, a))
        heapq.heapify(heap)

        ans = ""
        pre = []
        
        while heap:
            c, a = heapq.heappop(heap)
            ans += a
            if len(pre) != 0:
                heapq.heappush(heap, (pre[0], pre[1]))
                pre = []
            if c + 1 != 0:
                pre = [c + 1, a]
        
        if len(ans) == len(s):
            return ans
        return ""
                
        