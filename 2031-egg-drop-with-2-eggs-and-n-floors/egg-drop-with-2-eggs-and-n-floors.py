class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """

        def check(no, e, dp):
            if e == 1:
                return no 
            
            if no == 1 or no == 0:
                return no
            
            if (no, e) in dp:
                return dp[(no, e)]

            count = 10 ** 10
            for i in range(1, no + 1):
                willBreak = 1 + check(i - 1, e - 1, dp)
                notBreak = 1 + check(no - i, e, dp)
                count = min(count, max(willBreak, notBreak))
            
            dp[(no, e)] = count
            return count 
            

        return check(n, 2, {})
        