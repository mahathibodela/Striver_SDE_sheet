class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = 0
        h = len(nums) - 1
        n = len(nums) - 1
        while(l <= h):
            mid = (l + h) / 2
            print(mid, l, h)

            if(nums[mid] == target):
                return mid

            # left half is sorted
            elif(nums[l] <= nums[mid]):
                if(nums[l] <= target and target < nums[mid]):
                    h = mid - 1
                else:
                    l = mid + 1

            else:
                if(nums[mid] < target and target <= nums[h]):
                    l = mid + 1
                else:
                    h = mid - 1

        return -1

        
        