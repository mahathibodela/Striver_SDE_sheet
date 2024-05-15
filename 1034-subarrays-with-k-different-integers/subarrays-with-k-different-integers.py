class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def count(k):
            if k == 0: return 0

            l = 0
            freq = {}
            count = 0

            for i in range(len(nums)):
                no = nums[i]

                if no in freq:
                    freq[no] += 1
                else:
                    freq[no] = 1
                
                while len(freq) > k:
                    freq[nums[l]] = freq[nums[l]] - 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                
                count += i - l + 1
            
            return count

        return count(k) - count(k - 1)