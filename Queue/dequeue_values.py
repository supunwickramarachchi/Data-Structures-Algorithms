class Node:
	def __init__(self, value):
		self.value = value
		self.next = None 

class Queue:
	def __init__(self, value=None):
		new_node = Node(value)
		self.first = new_node
		self.last = new_node
		self.length = 1

	def print_queue(self):
		if self.length == 0:
			return "Queue is empty"

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

	def dequeue_value(self):
		if self.length == 0:
			return None 

		temp = self.first

		if self.length == 1:
			self.first = None
			self.last = None 

		else:
			self.first = self.first.next
			temp.next = None 

		self.length -= 1
		return temp


new_queue = Queue(4)
new_queue.enqueue_value(5)
new_queue.enqueue_value(6)
new_queue.enqueue_value(7)
new_queue.enqueue_value(8)

print(f"Removed Node: {new_queue.dequeue_value().value}")
print(f"Removed Node: {new_queue.dequeue_value().value}")
print(f"Removed Node: {new_queue.dequeue_value().value}")
print(f"Removed Node: {new_queue.dequeue_value().value}")
print(f"Removed Node: {new_queue.dequeue_value().value}")
print(f"Removed Node: {new_queue.dequeue_value()}")



new_queue.print_queue()
