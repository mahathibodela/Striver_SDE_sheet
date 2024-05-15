class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """


        def count(k):
            if k <0: return 0
            tot = 0
            l = 0
            ans = 0
            
            for i in range(len(nums)):
                tot += nums[i]
                while tot > k:
                    print(l, i)
                    tot -= nums[l]
                    l += 1
                ans += i - l + 1
            
            return ans
        
        return count(goal) - count(goal - 1)
                