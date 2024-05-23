class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        def isOk(i, j):
            s1 = words[i]
            s2 = words[j]
            if len(s1) - len(s2) != 1:
                return False

            n = len(s2)
            c = 0
            j = 0
            i = 0

            while j < n:
                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    c += 1
                    if c == 2:
                        return False
                    i += 1
            

            return True
            
     

        n = len(words)
        words.sort(key = lambda x : len(x))
        ans = 1
        dp = [1 for i in range(n)]

        for i in range(1, n):
            k = 1
            for j in range(i):
                if isOk(i, j):
                    k = max(k, dp[j] + 1)
            
            dp[i] = k
            ans = max(dp[i], ans)

        return ans

        



        return 0
        