import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        l = len(tasks)
        count = {}
        for i in tasks:
            if i in count:
                count[i] = count[i] + 1
            else:
                count[i] = 1
        
        heap = []
        for key, value in count.items():
            heap.append((-1 * value, key))

        heapq.heapify(heap)
        buffer = []
        time = 0

        while l != 0:
            if len(buffer) != 0 and time > buffer[0][1] + n:
                no, ind = buffer[0]
                buffer.pop(0)
                heapq.heappush(heap, no)
            
            if len(heap) != 0:
                freq, task = heapq.heappop(heap)
                freq += 1
                l -= 1
                if freq != 0:
                    buffer.append(((freq , task), time))
            
            time += 1

        return time

            
            
            

