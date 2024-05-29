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
            freqcount = {}
            alphacount = {}
            mini = 0
            maxi = 1
            freqcount[1] = 0
            for j in range(i, n):
                c = s[j]
                if c not in alphacount:
                    freqcount[1] += 1
                    alphacount[c] = 1
                    mini = 1
                else:
                    freqcount[alphacount[c]] -= 1
                    if freqcount[alphacount[c]] == 0 and alphacount[c] == mini:
                        mini += 1

                    alphacount[c] += 1
                    if alphacount[c] not in freqcount:
                        freqcount[alphacount[c]] = 1
                    else:
                        freqcount[alphacount[c]] += 1
                    maxi = max(alphacount[c], maxi)

                ans += maxi - mini
                   
        return ans


