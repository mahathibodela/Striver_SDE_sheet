class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.trail = Node(-1, -1)
        self.head.next = self.trail
        self.trail.pre = self.head
        self.map = {}
    
    def add(self, node):
        node.next = self.head.next
        node.next.pre = node
        self.head.next = node
        node.pre = self.head
    
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        
        node = self.map[key]
        self.remove(node)
        self.add(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            self.remove(self.map[key])
            self.capacity += 1
            del self.map[key]
        if self.capacity == 0:
            keyL = self.trail.pre.key
            self.remove(self.trail.pre)
            self.capacity += 1
            del self.map[keyL]

        
        node = Node(key, value)
        self.map[key] = node
        self.capacity -= 1
        self.add(node)

        return None


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)