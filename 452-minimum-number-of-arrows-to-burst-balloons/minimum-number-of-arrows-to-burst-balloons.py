class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        stack = []
        points.sort()
        for a, b in points:
            if stack and not stack[-1][1] < a:
                pa, pb = stack[-1]
                stack[-1] =[max(pa, a), min(pb, b)]
            else:
                stack.append([a, b])
        
        return len(stack)
            