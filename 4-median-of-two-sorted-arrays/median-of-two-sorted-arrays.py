class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if(n1 > n2) : return self.findMedianSortedArrays(nums2, nums1)

        n = n1 + n2 
        left = (n1 + n2 + 1) / 2
        l = 0
        h = n1 

        while(l <= h):
            mid = (l + h) / 2
            mid2 = left - mid

            l1 = -(10 ** 10)
            l2 = -(10 ** 10)
            r1 = (10 ** 10)
            r2 = (10 ** 10)

            if(mid > 0) : l1 = nums1[mid - 1]
            if(mid2 > 0): l2 = nums2[mid2 - 1]

            if(mid < n1): r1 = nums1[mid]
            if(mid2 < n2): r2 = nums2[mid2]

            if(max(l1, l2) <= min(r1, r2)):
                if((n1 + n2) % 2 == 0):
                    return (float((max(l1, l2)) + float(min(r1, r2))) / 2.0)
                else:
                    return max(l1, l2)
            
            if(l1 > l2 and l1 > min(r1, r2)):
                h = mid - 1
            elif(l2>l1 and l2 > min(r1, r2)):
                l = mid + 1
        
        return 0.0



        