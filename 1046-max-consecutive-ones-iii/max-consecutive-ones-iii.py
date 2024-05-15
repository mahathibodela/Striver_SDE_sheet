class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count=0
        st=0
        n=len(nums)
        ans=0

        for i in range(n):
            if nums[i]==0:
                count+=1
                if count>k:
                    ans=max(ans,i-st)
                    while count>k:
                        if nums[st]==0:
                            count-=1
                        st+=1
        
        if count<=k:
            ans=max(ans,n-st)
        return ans



        