class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        strs.sort()

        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        
        return strs[0]

        