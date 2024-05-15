class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        n = len(height)
        r = n - 1
        leftmax = rightmax = 0
        ans = 0

        while l<=r:
            if height[l] < height[r]:
                if height[l] >= leftmax:
                    leftmax = height[l]
                else:
                    ans += leftmax - height[l]
                
                l += 1
            else:
                if height[r] >= rightmax:
                    rightmax = height[r]
                else:
                    ans += rightmax - height[r]
                r -= 1
                
            
        
        return ans
        