class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        def check(i):
            temp = ""
            j = i
            while j < len(s):
                if s[j] != " ":
                    break
                else:
                    j += 1
            
            if j == len(s):
                return temp

            while j < len(s):
                if s[j] != " ":
                    temp += s[j]
                else:
                    break
                j += 1

            return check(j) + " "+ temp
    
        k = check(0)
        return k[1:]