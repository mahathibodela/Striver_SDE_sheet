class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tmap = {}
        for c in t:
            if c in tmap:
                tmap[c] += 1
            else:
                tmap[c] = 1
        
        def isSame(tmap, smap):
            if len(tmap) != len(smap): return False
            for key, values in tmap.items():
                if smap[key] - values < 0:
                    return False
            
            return True
        

        l = -1
        n = len(s)
        smap = {}
        r = 0
        ans = 10 ** 10
        ansStart = ansEnd = -1

        while r < n:
            c = s[r]
            if c in tmap:
                if l == -1:
                    l = r
                if c in smap:
                    smap[c] += 1
                else:
                    smap[c] = 1
            
                while isSame(tmap, smap) and l <= r:
                    if r - l + 1 < ans:
                        ans = r - l + 1
                        ansStart = l
                        ansEnd = r

                    if s[l] in tmap:
                        smap[s[l]] -= 1
                    l += 1     
            r += 1
            
        
        if ansStart != -1:
            return s[ansStart: ansEnd + 1]
        return ""

            

        