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

	def get_values(self, index):
		if index < 0 or index >= self.length:
			return True

		temp = self.head

		if index < self.length / 2:
			for _ in range(index):
				temp = temp.next
		else:
			temp = self.tail
			for _ in range(self.length - 1, index, -1):
				temp = temp.prev

		return temp

	def set_values(self, index, value):
		temp = self.get_values(index)

		if temp:
			temp.value = value
			return True

		return False


new_doubly_linkedlist = DoublyLinkedList(1)
new_doubly_linkedlist.append_values(2)
new_doubly_linkedlist.append_values(3)
new_doubly_linkedlist.prepend_values(0)

new_doubly_linkedlist.print_list()

print("After Change the value")

new_doubly_linkedlist.set_values(1, 5)
new_doubly_linkedlist.set_values(3, 7)

new_doubly_linkedlist.print_list()

