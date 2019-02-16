from binaryTree import  BinaryTree
class BinarySearchTree:
    def __init__(self, value):
        self.value = value 
        self.left_child = None 
        self.right_child = None 
    
    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)
    
    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)
        return value == self.value

    def find_minimum_value(self):
        if self.left_child:
            return self.left_child.find_minimum_value()
        else:
            return self.value

    def remove_node(self):
        if self is None:
            return None

        if value < self.value:
            self.left_child.remove_node(self.value)
        elif value > self.value:
            self.right_child.remove_node(self.value)
        else:
            if self.left_child is None:
                temp = self.right_child
                self.value = None
                return temp
            elif self.right_child is None:
                temp = self.left_child
                self.value = None
                return temp
            
            temp = find_minimum_value()
            self.right_child.remove_node(temp.value )
        
        return self








        

        

bst = BinarySearchTree(15)

bst.insert_node(10)
bst.insert_node(8)
bst.insert_node(12)
bst.insert_node(20)
bst.insert_node(17)
bst.insert_node(25)
bst.insert_node(19)

print(bst.find_node(15)) # True
print(bst.find_node(10)) # True
print(bst.find_node(8)) # True
print(bst.find_node(12)) # True
print(bst.find_node(20)) # True
print(bst.find_node(17)) # True
print(bst.find_node(25)) # True
print(bst.find_node(19)) # True

print(bst.find_node(0)) # False
