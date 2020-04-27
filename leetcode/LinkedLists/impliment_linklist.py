class Node:
	def __init__(self, item):
		self.item = item 
		self.next = None 


class UnorderdList:
	def __init__(self):
		self.head = None 
	
	def addNodeINFront(self, value):
		temp = Node(value)
		temp.next = self.head
		self.head = temp 
	
	def addNodeAtLast(self, value):
		current = self.head

		while current.next is not None:
			current = current.next
		
		temp = Node(value)
		temp.next = current.next
		current.next = temp 

	def PrintLinkedList(self):
		current = self.head 

		if self.head == None:
			print "empty Linked List"
		else:     
			while current.next is not None:
				print current.item
				current  = current.next 
			print current.item
	
	def deleteFrontNode(self):
		current = self.head 
		prev = None 

		if current.next == None:
			print "Empty LinkedList"
		else:
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
	

	def deleteANode(self, value):
		current = self.head 
		prev = None 

		while True:
			if current.item == value:
				break
			prev, current = current, current.next
			
		if prev == None:
			self.head = current.next
		else:
			prev.next = current.next
	
	def reverseLinkList(self):
		current = self.head 
		prev = None 
		while current.next is not None:
			pointer = current.next
			current.next = prev 
			prev = current
			current = pointer
		self.head = prev

	def reverseLLRecursive(self, current):
		if current.next is None:
			self.head = current
			return

		self.reverseLLRecursive(current.next)
		current.next.next = current 
		current.next = None


node = UnorderdList()

print "### add node infront"
node.addNodeINFront(10)
node.addNodeINFront(11)
node.addNodeINFront(12)
node.addNodeINFront(13)
node.addNodeINFront(14)
node.addNodeINFront(15)
node.addNodeINFront(16)

node.PrintLinkedList()
print ("\n")

print "### reverse a Linked List \n"
node.reverseLLRecursive(node.head)
node.PrintLinkedList()


print "### reverse a Linked List \n"
node.reverseLinkList()
node.PrintLinkedList()

print "### add node at last \n"
node.addNodeAtLast(1)
node.PrintLinkedList()
print ("\n")

print "### delete front Node \n"
node.deleteFrontNode()
node.PrintLinkedList()
print ("\n")

print "### delete Last Node \n"
node.deleteLastNode()
node.PrintLinkedList()
print ("\n")

print "### delete a given Node from the Linked - List \n"
node.deleteANode(12)
node.deleteANode(11)
node.PrintLinkedList()
print("\n")

