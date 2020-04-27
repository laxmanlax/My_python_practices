class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class UnorderdList:
    def __init__(self):
        self.head = None


    def addNodeINF(self, value):
        item = Node(value)
        item.next = self.head
        self.head = item

    def printLinkList(self):
        current = self.head

        while True:
            print current.item
            if current.next == None:
                break
            current = current.next

    def deleteAnode(self, value):
        current = self.head
        prev = None

        while True:
            if current.item == value:
                break

            prev, current = current, current.next

        if prev == None:
            self.head = current.next

    def deleteLastNode(self):
        current = self.head
        prev = None

        while True:
            if current.next == None:
                break

            prev, current = current, current.next

        if prev == None:
            self.head = current.next
        else:
            prev.next = current.next

    def deleteFirstNode(self):
        current = self.head
        if current.next == None:
            print "Link List is Empty"
        else:
            self.head = current.next

    def reverseLinkList(self):
        current = self.head
        prev = None

        while current.next is not None:
            pointer = current.next
            current.next = prev
            prev = current
            current = pointer

        self.head = prev




ans = UnorderdList()

ans.addNodeINF(10)
ans.addNodeINF(11)
ans.addNodeINF(12)
ans.addNodeINF(13)
ans.addNodeINF(14)
ans.addNodeINF(15)

ans.printLinkList()

print "\n"

ans.reverseLinkList()
ans.printLinkList()

print "\n"
ans.deleteLastNode()
ans.printLinkList()

print "\n"

ans.deleteFirstNode()
ans.printLinkList()

print "\n"

ans.reverseLinkList()
ans.printLinkList()
