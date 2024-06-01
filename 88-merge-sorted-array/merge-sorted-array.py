class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = n - 1
        for c in range(m, m + n):
            nums1[c] = -(10 ** 10)

        while i < m and j >= 0:
            if nums2[j] > nums1[i]:
                temp = nums1[i]
                nums1[i] = nums2[j]
                nums2[j] = temp
                i += 1
                j -= 1
            else:
                break
        
        nums1.sort()
        nums2.sort()
        print(nums1, nums2)
        for i in range(n):
            nums1[i] = nums2[i]
        
        return nums1
        
     

        