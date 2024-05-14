class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def find(k, ans, subans, tar, count):
            if tar == 0 and count == 0:
                temp = [b for b in subans]
                ans.append(temp)
                return 
            
            if k >= 10 or count <=0:
                return

            
            for i in range(k, 10):
                if i <= tar:
                    subans.append(i)
                    find(i + 1, ans, subans, tar - i, count - 1)
                    subans.pop(-1)

            find(i + 1, ans, subans, tar, count)
            return 
                
                


        ans = []
        find(1, ans, [], n, k)
        return ans
        