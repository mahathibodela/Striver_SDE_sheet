class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        lj

        """
            
        l,h=0,len(nums)-1

        while l<=h:
            mid=(l+h)/2

            if nums[mid]==target:
                return True
            while l <= h and nums[mid]==nums[l] and nums[mid]==nums[h] :
                l+=1
                h-=1
            
            if l > h:
                return False

            #this is left sorted
            elif nums[mid]>=nums[l]:
                if(target>=nums[l] and target<nums[mid]):
                    h=mid-1
                else:
                    l=mid+1
            #this is right sorted
            else:
                if(target>nums[mid] and target<=nums[h]):
                    l=mid+1
                else:
                    h=mid-1
        
        return False
