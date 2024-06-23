class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        fmax = nums[0]
        smax = -(10 ** 10)
        c = 1


        for i in range(1, len(nums)):
            no = nums[i]
            # print(no, fmax, smax, c)
            if smax > no:
                if c == 0:
                    return False
                smax = no
                c -= 1
            
            elif fmax > no:
                if c == 0:
                    return False
                fmax = max(smax, no)
                smax = min(smax, no)
                c -= 1
            
            else:
                if no > fmax:
                    smax = fmax
                    fmax = no
                elif no > smax:
                    smax = no
        
        return True
