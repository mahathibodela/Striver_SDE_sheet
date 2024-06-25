class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        if num <= 11:
            return num
        
        nums_as_arr = collections.deque([])
        while num:
            nums_as_arr.appendleft(num%10)
            num = num / 10
        
        maxSeen = -1
        maxSeenAt = -1
        i = len(nums_as_arr) - 1

        while i >= 0:
            cur_num = nums_as_arr[i]
            nums_as_arr[i] = (cur_num, maxSeen, maxSeenAt)

            if cur_num > maxSeen:
                maxSeen = cur_num
                maxSeenAt = i
            i -= 1
        
        i = 0
        while i < len(nums_as_arr):
            cur_num, max_to_right, max_seen_at = nums_as_arr[i]

            if max_to_right > cur_num:
                nums_as_arr[i], nums_as_arr[max_seen_at] = nums_as_arr[max_seen_at], nums_as_arr[i]
                break
            i += 1
        
        num = 0
        for cur_num, _, _ in nums_as_arr:
            num = num * 10 + cur_num
        return num
