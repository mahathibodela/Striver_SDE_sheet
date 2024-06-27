class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = ""
        stack.append("/")
        if path[-1] != '/':
            path += '/'
        
        i = 1
        while i < len(path):
            c = path[i]
            if c != '/':
                temp += c
            else:
                if len(temp) == 0 or temp == "." or (len(stack) < 3 and temp == ".."):
                    pass
                elif len(stack) >= 3 and temp == "..":
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(temp)
                    stack.append("/")
                
                temp = ""
            i += 1
        
        if temp != "":
            stack.append(temp)
        
        ans = ""
        while stack:
            temp = stack.pop()
            ans = temp + ans
        
        if len(ans) != 1 and ans[-1] == '/':
            ans = ans[:-1]
        
        return ans

