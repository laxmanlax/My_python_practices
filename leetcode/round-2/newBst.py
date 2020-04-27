class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


	def insertNode(self, value):
		if value < self.value:
			if self.left:
				self.left.insertNode(value)
			else:
				self.left = BinaryTree(value)
		else:
			if self.right:
				self.right.insertNode(value)
			else:
				self.right = BinaryTree(value)


	def pre_order(self):
		print self.value

		if self.left:
			self.left.pre_order()
		if self.right:
			self.right.pre_order()


	def in_order(self):

		if self.left:
			self.left.in_order()

		print self.value

		if self.right:
			self.right.in_order()


	def post_order(self):
		if self.left:
			self.left.post_order()

		if self.right:
			self.right.post_order()


		print self.value


	def find_node(self, value):
		if value = self.value:
			return True

		if value < self.value:
			if self.left:
				self.left.find_node(value)
			else:
				return False
		else:
			if self.right:
				self.right.find_node(value)
			else:
				return False



	def bfs(self):

		queue = Queue()
		queue.put(self)

		while not queue.empty():
			current_node = queue.get()
			print current_node

			if current_node.left:
				queue.put(self.left)

			if current_node.right:
				queue.put(self.right)
