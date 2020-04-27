class Node:
#https://www.youtube.com/watch?v=7v_mUfpg46E&feature=youtu.be
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, func):
        self.capacity = capacity
        self.D = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.next = self.next


    def get(self, key):
        if ( key in self.D ) == False:
            return -1

        n = self.D[key]
        self._remove(n)
        self.add(n)
        return n.val

    def put(self, key, value):
        if key in self.D:
            self._remove(self.D[key])
            del self.D[key]
        elif len(self.D)  == len(self.capacity): # capacity reached
            n = self.head.next
            self._remove(n)
            del self.D[n.key]

        # Adding item to the LRU cache
        n = Node(key, value)
        self.D[key] = n
        self._add(n)


    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node


    def _remove(self, node):
        p = node.prev
        p.next = node.next
        node.next.prev = p
