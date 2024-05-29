class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """

        def check(count):
            maxi = 0
            mini = (10 ** 10)

            for key, value in count.items():
                maxi = max(value, maxi)
                mini = min(value, mini)
            
            return maxi - mini
        
        ans = 0
        n = len(s)
        for i in range(n):
            count = {}
            for j in range(i, n):
                c = s[j]
                if c not in count:
                    count[c] = 1
                else:
                    count[c] += 1
                
                ans += check(count)
        
        return ans


