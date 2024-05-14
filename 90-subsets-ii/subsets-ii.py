class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def find(i, ans, subans):

            if i == len(nums):
                b = [k for k in subans]
                ans.append(b)
                return
            
            for j in range(i, len(nums)):
                if i == j or nums[j] != nums[j - 1]:
                    subans.append(nums[j])
                    find(j + 1, ans, subans)
                    subans.pop(-1)
        
            find(len(nums), ans, subans)



        nums.sort()
        ans = []
        find(0, ans, [])
        return ans