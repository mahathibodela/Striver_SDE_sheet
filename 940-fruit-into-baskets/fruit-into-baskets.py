class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        def getMin(has):
            k = " "
            c = 10 ** 10
            for key in has:
                if has[key] < c:
                    c = has[key]
                    k = key
            
            return k

        has = {}
        l = 0
        ans = 0

        for r in range(len(fruits)):
            f = fruits[r]
            has[f] = r

            if len(has) > 2:
                c = getMin(has)
                temp = has[c] + 1
                del has[c]
                l = temp
            
            ans = max(ans, r - l + 1)
        
        return ans
            
            