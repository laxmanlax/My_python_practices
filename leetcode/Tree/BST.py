class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

    def insert_node(self, value):
        if value <= self.value:
            if self.value:
                self.left.insert_node(value)
            else:
                self.left = BinaryTree(value)
        else:
            if self.right:
                self.right.insert_node(value)
            else:
                self.right = BinaryTree(value)

    
    def pre_order(self):
        print self.value 

        if self.left:
            self.left.pre_order()
        
        if self.right:
            self.right.pre_order()
        
    
    def in_order(self):
        if self.left:
            self.left.in_order()
        
        print self.value

        if self.right:
            self.right.in_order()
    
    def post_order(self):
        if self.left:
            self.left.post_order()
        
        if self.right:
            self.right.post_order()

        print self.value
    
    def find(self. data):
        if data == self.data:
            return True
        
        if data < self.data:
            if self.left:
                self.left.find(data)
            else:
                return False
        else:
            if self.right:
                self.right.find(data)
            else:
                return False
    

    def find_node(self, value):
        if  value < self.value and self.left:
            self.left.find_node(value)
        
        if value > self.value and self.right:
            self.right.find_node(value)
        
        return value = self.value
    



    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            curr = queue.get()
            print curr

            if curr.left:
                queue.put(self.left)
            
            if curr.right:
                queue.put(self.right)
