class FreqStack(object):

    def __init__(self):
        self.freq = collections.defaultdict(list)
        self.max_count = 0
        self.map = {}

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.map:
            self.map[val] = self.map[val] + 1
        else:
            self.map[val] = 1
        
        self.max_count = max(self.max_count, self.map[val])
        self.freq[self.map[val]].append(val)

    def pop(self):
        """
        :rtype: int
        """
        val = self.freq[self.max_count].pop(-1)
        self.map[val] = self.map[val] - 1

        if len(self.freq[self.max_count]) == 0:
            self.max_count = self.max_count - 1
        
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()