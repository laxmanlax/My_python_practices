class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class NewLinkList:
    def __init__(self):
        self.head = None


    def addNewNode(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def PrintLinkList(self):
        current = self.head

        while True:
            print current.item
            if current.next == None:
                break
            current = current.next

    def revers_LinkList(self):
        current = self.head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def deleteANode(self, val):
        current = self.head
        prev = None

        while True:
            if current.item == val:
                break

            prev, current = current , current.next

        if prev == None:
            self.head = current.next
        else:
            prev.next = current.next

    def is_circuler(head):
        slow = head
        fast = head

        while fast! = None:
            slow = slow.next

            if fast.next!=None:
                fast = fast.next.next
            else:
                return False

        if slow == fast:
            return True







node = NewLinkList()

node.addNewNode(1)
node.addNewNode(2)
node.addNewNode(3)
node.addNewNode(4)
node.addNewNode(5)

node.PrintLinkList()
print "\n"

node.revers_LinkList()
node.PrintLinkList()
print "\n"

node.deleteANode(4)
node.PrintLinkList()
