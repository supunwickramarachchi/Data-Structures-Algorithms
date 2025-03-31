class Node:
	def __init__(self, value):
		self.value = value
		self.next = None 

class Queue:
	def __init__(self, value):
		new_node = Node(value)
		self.first = new_node
		self.last = new_node
		self.length = 1

	def print_queue(self):
		temp = self.first
		while temp is not None:
			print(temp.value)
			temp = temp.next

	def enqueue_value(self, value):
		new_node = Node(value)

		if self.first is None:
			self.first = new_node
			self.last = new_node
		else:
			self.last.next = new_node
			self.last = new_node

		self.length += 1

new_queue = Queue(4)
new_queue.enqueue_value(5)
new_queue.enqueue_value(6)

new_queue.print_queue()
