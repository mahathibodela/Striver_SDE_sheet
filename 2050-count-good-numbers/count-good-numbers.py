class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 5
        mod = 10 ** 9 + 7
        odd = n / 2
        even = n - (n / 2)

        def power(x, no):
            if no == 0:
                return 1
            
            smallP = power(x, no/2)
            if no % 2 == 0:
                return ((smallP % mod) * (smallP % mod)) % mod
            else:
                return ((x * (smallP % mod)) * (smallP % mod)) % mod
            
            return 0
           
        return (power(5, even) * power(4, odd)) % mod