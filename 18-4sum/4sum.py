class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                curSum = target - nums[j] - nums[i]

                l = j + 1
                r = n - 1

                while l < r:
                    c = nums[l] + nums[r]
                    if c == curSum:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]: l += 1
                        while l < r and nums[r] == nums[r + 1]: r -= 1
                    elif c < curSum:
                        l += 1
                    else:
                        r -= 1

        
        return ans

                
        