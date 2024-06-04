class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        pairs = []
        for i in range(len(nums1)):
            pairs.append((nums2[i], nums1[i]))
        
        pairs.sort(reverse = True)
        heap = []
        heapq.heapify(heap)
        totSum = 0
        ans = 0
        # heap main (nums1, nums2) jayega

        for a, b in pairs:
            heapq.heappush(heap, (b, a))
            totSum += b

            if len(heap) == k:
                ans = max(ans, a * totSum)
                nums2no, num1no = heapq.heappop(heap)
                totSum -= nums2no
        
        return ans

            