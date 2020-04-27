class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class ImplLinkList:
    def __init__(self):
        self.head = None


    def addNode(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def PrintLinkList(self):
        current = self.head

        while True:
            print current.item
            current = current.next
            if current == None:
                break

    def reverseLink(self):
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

        while current or current.next:
            if current.val == val:
                break

            prev , current = current, current.next

        if prev:
            prev.next = current.next
        else:
            self.heaf = current.next

    def is_circuler(head):
        slow = head
        fast = head

        while fast!=None:
            slow = slow.next

            if fast.next!=None:
                fast = fast.next.next
            else:
                return False

            if slow == fast:
                return True



node1 = ImplLinkList()

node1.addNode(1)
node1.addNode(2)
node1.addNode(3)
node1.addNode(4)
node1.addNode(5)
node1.addNode(6)
node1.addNode(7)

node1.PrintLinkList()

node1.reverseLink()

print "After -- reverseLink \n"

node1.PrintLinkList()
