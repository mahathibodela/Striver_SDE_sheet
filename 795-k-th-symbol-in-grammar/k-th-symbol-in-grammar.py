class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        def check(np, kp):
            if np == 1:
                return 0
            
            ind = int(math.ceil(kp/2.0))
            if ind == 0: ind = 1
            no = check(np - 1, ind)
            # print(no, ind, np)

            if kp % 2 != 0:
                if no == 1:
                    return 1
                return 0
            else:
                if no == 1:
                    return 0
                return 1
            
        # print(int(math.ceil(3/2.0)))
        ans = check(n, k)
        return ans