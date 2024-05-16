class StockSpanner(object):

    def __init__(self):
        self.stack = []
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        count = 1
        while len(self.stack) != 0 and self.stack[-1][0] <= price:
            _, pre = self.stack[-1]
            count += pre
            self.stack.pop(-1)
        self.stack.append((price, count))
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)