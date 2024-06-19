class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s): return []

        l = 0
        pcount = collections.defaultdict(int)
        scount = collections.defaultdict(int)

        for i in range(len(p)): 
            pcount[p[i]] += 1
            scount[s[i]] += 1

        ans = [0] if pcount == scount else []

        for r in range(len(p), len(s)):
            scount[s[r]] += 1
            scount[s[l]] -= 1

            if scount[s[l]] == 0:
                del scount[s[l]]
            l += 1
            if scount == pcount:
                ans.append(l)
        
        return ans
