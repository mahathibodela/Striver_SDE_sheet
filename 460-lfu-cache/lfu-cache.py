class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None
        self.count = 1

class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.size = 0

        self.head.next = self.tail
        self.tail.pre = self.head
    
    def add(self, node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node
        self.size += 1
    
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = None
        node.next = None
        self.size -= 1

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.freq = {} # count - DLL
        self.min = 1
        self.map = {}  # key - node
        self.cap = capacity
    
    def update(self, node):
        self.freq[node.count].remove(node)
        if self.freq[node.count].size == 0 and node.count == self.min:
            self.min += 1
        node.count += 1
        if node.count not in self.freq:
            self.freq[node.count] = DLL()
        self.freq[node.count].add(node) 

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map: return -1

        node = self.map[key]
        self.update(node)
        return node.val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.update(node)
        else:
            if self.cap == 0:
                node = self.freq[self.min].tail.pre
                self.freq[node.count].remove(node)
                del self.map[node.key]
            else:
                self.cap -= 1
            
            node = Node(key, value)
            self.map[key] =  node
            if 1 not in self.freq:
                self.freq[1] = DLL()
            self.freq[1].add(node)
            self.min = 1
        
        print(self.min)
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)