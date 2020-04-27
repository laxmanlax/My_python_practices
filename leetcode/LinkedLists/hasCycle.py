class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


    def setNext(self, next_node=None):
        self.next = next_node


    def printList(self):
        current = self.next

        while True:
            if current.next == None:
                break
            print current.data
            current = current.next



def is_circuler(head):
    slow = head
    fast = head

    while fast !=None:
        slow = slow.next

        if fast.next != None:
            fast = fast.next.next
        else:
            return False

    if slow is fast:
        return True
