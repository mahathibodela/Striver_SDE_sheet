class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        h = len(arr) - 1

        if arr[h] - (h + 1) < k:
            return arr[h] + k - (arr[h] - (h + 1))
        if arr[l] - 1 >= k:
            return k

        while l <= h:
            mid = (l + h) / 2
            print(mid)

            if (arr[mid] - (mid + 1)) >= k:
                h = mid - 1
            else:
                l = mid  + 1
        
        print(h)
        return arr[h] + k - (arr[h] - (h + 1))
        