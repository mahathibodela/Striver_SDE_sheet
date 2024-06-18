class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        options=[str(i) for i in range(10)]
        ans=[]
        i=1

        def check(no,ans):
            if int(no)>n:
                return 
            
            ans.append(int(no))
            for option in options:
                check(no+option,ans)
                       
        for i in range(1,10):
            if i<=n:
                check(str(i),ans)
            else:
                break

        return ans
    