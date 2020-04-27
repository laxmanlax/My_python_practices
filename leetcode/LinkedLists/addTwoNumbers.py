class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class List1:
    def __init__(self):
        self.head = None

    def addNodeinLL(self, item):
        temp = Node(item)
        temp.next = self.head 
        self.head = temp 


class List2:
    def __init__(self):
        self.head = None
        
    def addNodeinLL(self, item):
        temp = Node(item)
        temp.next = self.head 
        self.head = temp


userInput = raw_input()
