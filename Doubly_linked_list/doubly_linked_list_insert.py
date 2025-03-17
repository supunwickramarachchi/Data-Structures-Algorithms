class Node:
	def __init__(self, value):
		self.value = value
		self.next = None 
		self.prev = None

class DoublyLinkedList:
	def __init__(self, value):
		new_node = Node(value)
		self.head = new_node
		self.tail = new_node
		self.length = 1

	def print_list(self):
		temp = self.head

		while temp is not None:
			print(temp.value)
			temp = temp.next

	def append_values(self, value):
		new_node = Node(value) 

		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			new_node.prev = self.tail
			self.tail = new_node

		self.length += 1
		return True

	def prepend_values(self, value):
		new_node = Node(value)

		if self.length == 0:
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node

			self.length += 1
			return True

	def insert_value(self, index, value):
		if index < 0 or index > self.length:
			return None 

		if index == 0:
			return self.prepend_values(value)

		if index == self.length:
			return self.append_values(value)

		new_node = Node(value)
		before = self.get_values(index - 1)
		after = before.next

		new_node.prev = before
		new_node.next = after
		before.next = new_node
		after.prev = new_node

		self.length += 1
		return True
 

new_doubly_linkedlist = DoublyLinkedList(1)
new_doubly_linkedlist.append_values(2)
new_doubly_linkedlist.prepend_values(0)
new_doubly_linkedlist.insert_value(3, 3)


new_doubly_linkedlist.print_list()

