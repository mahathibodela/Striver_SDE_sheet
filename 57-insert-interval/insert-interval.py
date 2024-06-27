class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        ans = []
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                ans.append(newInterval)
                return ans + intervals[i:]
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        
        ans.append(newInterval)
        return ans
        