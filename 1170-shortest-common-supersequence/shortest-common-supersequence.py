class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        text1 = str1
        text2 = str2
        def check(i, j, dp):
            if i >= n or j >= m:
                dp[(i, j)] = 0
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if text1[i] == text2[j]:
                k = 1 + check(i + 1, j + 1, dp)
            else:
                k = max(check(i + 1, j, dp) , check(i, j + 1, dp))

            dp[(i, j)] = k
            return k

        n = len(text1)
        m = len(text2)
        dp = {}
        k = check(0, 0, dp)

        i = j = 0
        ind1 = []
        ind2 = []

        while i < n and j < m:
            if text1[i] == text2[j]:
                ind1.append(i)
                ind2.append(j)
                i += 1
                j += 1
            else:
                if dp[(i + 1, j)] > dp[(i, j + 1)]:
                    i += 1
                else:
                    j += 1
        
        if len(ind1) == 0:
            return str1+str2

        ind1.append(n)
        ind2.append(m)
        ans = ""
        i = 0 
        aprev = bprev = 0
        a = b = 0
        while i < len(ind1):
            a = ind1[i]
            b = ind2[i]
            ans += text1[aprev:a]
            ans += text2[bprev:b]
            if i != len(ind1) - 1:
                ans += text1[a]

            aprev = a + 1
            bprev = b + 1
            i += 1
        
        return ans
       

        