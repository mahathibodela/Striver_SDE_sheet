class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        l = m + n - 1
        m = m - 1
        n -= 1

        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[l] = nums1[m]
                m -= 1
            else: 
                nums1[l] = nums2[n]
                n -= 1
            l -= 1
            
        while n >= 0:
            nums1[l] = nums2[n]
            n -= 1
            l -= 1
        