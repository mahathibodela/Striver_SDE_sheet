class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        l = 0
        r = 1
        c = 1
        n = len(chars)

        while r < n:
            if chars[r] != chars[l]:
                if c != 1:
                    for i in (str(c)):
                        l += 1
                        chars[l] = i
                l += 1
                chars[l] = chars[r]
                c = 0
            c += 1
            r += 1
        
        if c == 1: return l + 1
        for i in (str(c)):
            l += 1
            chars[l] = i 
        return l + 1

