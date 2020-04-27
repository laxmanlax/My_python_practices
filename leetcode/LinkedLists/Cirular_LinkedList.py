class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def setNext(self, next_node=None):
        self.next = next_node

    def PrintList(self):
        current = self.next
        print current.data
        while current.next is not None:
            current = current.next
            print current.data

def has_cycle(head):
    if head == None:
        return False
    fast = head
    slow = head

    while (slow or fast or fast.next):
        if fast.next == None:
            return False

        if slow == fast.next or slow == fast.next.next:
            return True

        slow = slow.next
        fast = fast.next.next

    return False


def is_circular(head):
    slow = head
    fast = head

    while fast != None:
        slow = slow.next
        print slow.data ,"--->>", fast.data

        if fast.next !=None:
            fast = fast.next.next
        else:
            return False

        if slow is fast:
            print "Circular......."
            return True




def intersection_point1(node1, node2):
	link1 = node1
	link2 = node2

	while link1.next is not None or link2.next is not None:
		print link1.data, "------>>", link2.data
		link1 = link1.next
		link2 = link2.next


def intersection_point(node1, node2):
    link1 = node1
    link2 = node2

    while link1.next is not None or link2.next is not None:
        print link1.data, "------>>", link2.data
        if link1.next == link2.next:
            break

        link1 = link1.next
        link2 = link2.next


n1 = Node(1, None)
n2 = Node(2, n1)
n3 = Node(3, n2)
n4 = Node(4, n3)
n5 = Node(5, n4)
n6 = Node(6, n5)
n7 = Node(7, n6)
n8 = Node(8, n7)
n9 = Node(9, n8)
n10 = Node(10, n9)
n11 = Node(11, n10)
n12 = Node(12, n11)
n13 = Node(13, n12)
n14 = Node(14, n13)
n15 = Node(15, n14)
n16 = Node(16, n15)
n17 = Node(17, n16)

## create a circular linked List
## n1.setNext(n17)

## verify a circular
## print has_cycle(n3)
## print is_circular(n1)

m1 = Node(1, None)
m2 = Node(2, m1)
m3 = Node(3, m2)
m4 = Node(4, m3)
m5 = Node(5, m4)
m6 = Node(6, m5)
m7 = Node(7, m6)
m8 = Node(8, m7)
m9 = Node(9, m8)
m10 = Node(10, m9)
m11 = Node(11, m10)
m12 = Node(12, m11)
m13 = Node(13, m12)
m14 = Node(14, m13)
m15 = Node(15, m14)
m16 = Node(16, m15)
m17 = Node(17, m16)


a1 = Node(1, None)
a2 = Node(2, a1)
a3 = Node(3, a2)
a4 = Node(4, a3)
a5 = Node(5, a4)
a6 = Node(6, a5)

### find intersection point
m10.setNext(a6)
n10.setNext(a6)

intersection_point1(m17, n17)
