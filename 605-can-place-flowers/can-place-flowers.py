class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        ans = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                    n -= 1
                    i += 1
                elif i == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    i += 1
                elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    i += 1
            i += 1
            print(i)
        
        return n <= 0