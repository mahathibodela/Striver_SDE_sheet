class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)
        l = 0
        r = n - 1
        res = 0

        while l < r:
            ans = min(height[r], height[l])
            res = max(res, ans * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res
