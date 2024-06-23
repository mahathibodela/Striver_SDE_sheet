class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        def floor():
            l = 0
            h = n - 1

            while l <= h:
                mid = (l + h) /2
                if arr[mid] == x:
                    return mid
                if arr[mid] < x:
                    l = mid + 1
                else:
                    h = mid - 1
            return h
        
        def ceil():
            l = 0
            h = n - 1

            while l <= h:
                mid = (l + h) /2
                if arr[mid] == x:
                    return mid
                if arr[mid] <= x:
                    l = mid + 1
                else:
                    h = mid - 1
            return l

        n = len(arr)
        l = floor()
        h = ceil()

        if l == h:
            l -= 1
            h += 1
            k -= 1
        
        # print(l, h)
        while (l >= 0 or h < len(arr)) and k != 0:
            if h >= n or (l >= 0 and abs(arr[l] - x) <= abs(arr[h] - x)):
                l -= 1
            else:
                h += 1
            k -= 1
        
        ans = []
        for i in range(l + 1, h):
            ans.append(arr[i])
        
        return ans