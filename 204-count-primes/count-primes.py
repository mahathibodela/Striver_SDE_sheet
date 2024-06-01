class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = n - 1
        isPrime = [1 for i in range(n + 1)]
        
        i = 2
        while i * i <= n:
            if isPrime[i] == 1:
                j = i
                while j * i <= n:
                    isPrime[j * i] = 0
                    j += 1
            i += 1
        
        c = 0
        for i in range(2, n + 1):
            if isPrime[i] == 1:
                c += 1
        
        return c


        