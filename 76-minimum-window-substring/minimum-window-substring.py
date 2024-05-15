class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        def isSame(tdict, sdict):
            for i in tdict:
                if i not in sdict or sdict[i] - tdict[i] < 0:
                    return False
            
            return True


        l = -1
        tdict = {}
        sdict = {}
        ans = 10 ** 10
        sans = -1
        send = -1

        for i in t:
            if i in tdict:
                tdict[i] += 1
            else:
                tdict[i] = 1
        
        for i in range(len(s)):
            c = s[i]
            if c in tdict:
                if l == -1:
                    l = i
                
                if c in sdict:
                    sdict[c] += 1
                else:
                    sdict[c] = 1
            
            while isSame(tdict, sdict):
                if i - l + 1 < ans:
                    sans = l
                    send = i
                    ans = i - l + 1
                
                z = s[l]
                if z in tdict:
                    sdict[s[l]] -= 1
                l += 1
                
            
        return s[sans : send + 1]
