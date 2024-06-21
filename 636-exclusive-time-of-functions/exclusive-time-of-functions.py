class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        t = 0
        logM = []
        for log in logs:
            a, b, c = log.split(":")
            logM.append((int(a), str(b), int(c)))
        
        # logM.sort(key = lambda x:x[2])
        ans = [0 for i in range(n)]

        stack = [logM[0]]
        for i in range(1, len(logM)):
            if logM[i][1] == "start":
                if stack:
                    ans[stack[-1][0]] += logM[i][2] - t
                t = logM[i][2]
                stack.append(logM[i])
            else:
                ans[stack[-1][0]] += logM[i][2] - t + 1
                stack.pop(-1)
                t = logM[i][2] + 1
        
        return ans
