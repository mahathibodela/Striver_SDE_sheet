class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[0 for i in range(n2)] for i in range(n1)]
        ans = 0

        for i in range(n1):
            for j in range(n2):
                if i == 0 or j == 0:
                    if nums1[i] == nums2[j]:
                        dp[i][j] = 1
                else:
                    if nums1[i] == nums2[j]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
            
                ans = max(ans, dp[i][j])
        
        return ans
        
                    