class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def check(no):
            if no == 1:
                return "1"
            
            num = check(no - 1)
            ans = ""
            l = 0 
            r = 1
            # print(no, num)
            while r < len(num):
                if num[r] == num[r - 1]:
                    r += 1
                    continue
                ans += str((r - l)) + num[l]
                l = r
                r += 1
                
            ans += str((r - l)) + num[l]
            print(no, num, ans)
            return ans

        k = check(n)
        return k
        