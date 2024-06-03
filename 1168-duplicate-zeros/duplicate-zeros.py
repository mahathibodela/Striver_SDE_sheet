class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        c = 0
        one = False
        l = 0

        for i in range(n):
            if arr[i] == 0:
                c += 1
            if c == n:
                one = True
                l = i
                break
            c += 1
            if c == n:
                l = i
                break

        
        h = n - 1

        while l >= 0 and h >= 0:
            if one == True:
                arr[h] = 0
                h -= 1
                l -= 1
                one = False
            else:
                arr[h] = arr[l]
                h -= 1
                l -= 1
                if arr[l + 1] == 0:
                    arr[h] = 0
                    h -= 1
                

        
            
        

        
