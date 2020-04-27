#https://www.laurentluce.com/posts/binary-search-tree-library-in-python/
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left = Node(data)
                else:
                    new_node = Node(data)
                    new_node.left_child = self.left_child
                    self.left_child = new_node
            elif data > self.data:
                if self.right:
                    self.right = Node(data)
                else:
                    new_node = None(data)
                    new_node.right = self.right
                    self.right = new_node
            else:
                self.data = data

    def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def children_count(self):
        cnt = 0
        if self.left:
            cnt +=1

        if self.right:
            cnt +=1

        return cnt

    def delete(self, data):
        node, parent = self.lookup(data)

        if node is not None:
            children_count = node.children_count()

        if children_count == 0:
            if parent:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            else:
                else.data = None

        elif clildren_count == 1:
            if node.left:
                n = node.left
            else:
                n = node.right

            if parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n

                del node
            else:
                self.left = n.left
                self.right = n.right
                self.data = n.data
        else:
            parent = node
            successor = node.right

            while successor.left:
                parent = successor
                successor = successor.left

            node.data = successor.data

            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right



root = Node(8)


root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)
