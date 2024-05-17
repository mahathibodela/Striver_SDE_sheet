class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False

        count = {}
        heap = []
        for no in hand:
            if no in count:
                count[no] += 1
            else:
                count[no] = 1
                heap.append(no)

        heapq.heapify(heap)

        while len(heap) != 0:
            no = heap[0]

            for i in range(no, no + groupSize):
                if i in count:
                    count[i] -= 1
                    if count[i] == 0:
                        if i == heap[0] :
                            d = heapq.heappop(heap)
                            del count[i]
                        else:
                            return False
                else:
                    return False
        
        return True

        
        

        

    


        