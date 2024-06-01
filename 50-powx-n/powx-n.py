class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        sign = True
        if n < 0 : sign = False
        n = abs(n)
        ans = 1.0

        while n > 0:
            if n == 1:
                ans = ans * x
                if sign == True:
                    return ans
                return 1/ans

            if n % 2 == 0:
                x = x * x
                n = n / 2
            else:
                ans = ans * x
                n = n - 1
        
        return ans



        