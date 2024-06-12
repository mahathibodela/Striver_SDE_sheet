class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """

        stack = []
        c = 0
        for no in pushed:
            stack.append(no)

            while stack and c < len(popped) and popped[c] == stack[-1]:
                a = stack.pop(-1)
                c += 1
        
        if len(stack) == 0:
            return True
        return False


        