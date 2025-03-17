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


	def get_values(self, index):
		if index < 0 or index >= self.length:
			return None 

		temp = self.head

		if index < self.length / 2:
			for _ in range(index):
				temp = temp.next
		else:
			temp = self.tail
			for _ in range(self.length - 1, index, -1):
				temp = temp.prev

		return temp

	def get_value(self, index):
		if index < 0 or index >= self.length:
			return None 

		temp = self.head 

		if index < self.length / 2:
			for _ in range(index):
				temp = temp.next 
		else:
			temp = self.tail
			for _ in range(self.length - 1, index, -1):
				temp = temp.prev

		return temp


new_doubly_linked_list = DoublyLinkedList(1)
new_doubly_linked_list.append_values(2)
new_doubly_linked_list.append_values(3)
new_doubly_linked_list.append_values(4)
new_doubly_linked_list.append_values(5)

new_doubly_linked_list.print_list()

print(f"Requested Number: {new_doubly_linked_list.get_values(3).value}")
