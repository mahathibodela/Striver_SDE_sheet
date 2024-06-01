class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def check(o, c, ans, s):
            if c < o or (o < 0) or (c < 0):
                return 
            
            if c == 0 and o == 0:
                ans.append(s)
                return
            
            check(o - 1, c, ans, s + "(")
            check(o, c - 1, ans, s + ")")

        ans = []
        check(n, n, ans, "")
        return ans

        