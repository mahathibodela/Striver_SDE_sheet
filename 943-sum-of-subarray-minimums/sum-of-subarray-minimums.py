class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        nums = arr
        rightSmall = [n for i in range(n)]
        leftSmall = [-1 for i in range(n)]
        stack = []
        mod = 1e9 + 7

        for i in range(n):
            no = arr[i]
            while len(stack) != 0 and nums[stack[-1]] >= no:
                j = stack[-1]
                rightSmall[j] = i
                stack.pop(-1)
            stack.append(i)
        
        stack = []
        for i in range(n -1, -1, -1):
            no = arr[i]
            while len(stack) != 0 and nums[stack[-1]] > no:
                j = stack[-1]
                leftSmall[j] = i
                stack.pop(-1)
            stack.append(i) 

        print(rightSmall, leftSmall)
        ans = 0
        for i in range(n):
            ls = leftSmall[i] + 1
            rs = rightSmall[i] - 1
            ln = (i - ls + 1) % mod
            rn = (rs - i + 1) % mod
            mn = ((ln + 1) * (rn + 1)) % mod
            
            print(i, ln, rn, mn)
            # ans += int((arr[i] * (ln + rn + mn - 1)) % (1e9 + 7))/
            ans = int(ans % mod) + int((nums[i] * ln * rn) % mod)
        return ans