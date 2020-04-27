 class BinaryTree:
     def __init__(self, value):
         self.value = value
         self.left_child = None
         self.right_child = None

    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value < self.value:
            self.left_child = BinaryTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_right(value)
        else:
            self.right_child = BinaryTree(value)

    def insert(self, value):
        if value < self.value:
            if self.left_child:
                self.left_child.insert(value)
            else:
                self.left_child = BinaryTree(value)
        else:
            if self.right_child:
                self.right_child.insert(value)
            else:
                self.right_child = BinaryTree(value)


    def pre_order(self):
        print self.value

        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()


    def in_order(self):
        if self.left_child:
            self.left_child.in_order()

        print self.value

        if self.right_child:
            self.right_child.in_order()


    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()

        print self.value

    def find(self, data):
        if data == self.data:
            return True
        elif data < self.data:
            if self.left_child:
                self.left_child.find(data)
            else:
                return False
        else:
            if self.right_child:
                self.right_child.find(data)
            else:
                return False

    def find_node(self, value):
        if value < self.value and self.left_child:
            self.left_child.find_node(value)

        if value > self.value and self.right_child:
            self.right_child.find_node(value)

        return value == self.value


def bfs(self):
    queue = Queue()
    queye.put(self)

    while not queue.empty():
        courr = queue.get()
        print courr

        if courr.left_child:
            queue.put(self.left_child)

        if courr.right_child:
            queue.put(self.right_child)
