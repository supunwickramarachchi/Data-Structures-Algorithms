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

	def pop_values(self):
		if self.length == 0:
			return None 

		temp = self.tail 

		if self.length == 1:
			self.head = None 
			self.tail = None

		else:
			self.tail = self.tail.prev
			self.tail.next = None 
			temp.prev = None 

		self.length -= 1
		return temp

	def pop_first_value(self):
		if self.length == 0:
			return None

		temp = self.head

		if self.length == 1:
			self.head = None 
			self.tail = None 

		else:
			self.head = self.head.next
			self.head.prev = None 
			temp.next = None 

		self.length -= 1
		return temp

	def remove_items(self, index):
		if index < 0 or index >= self.length:
			return None

		if index == 0:
			return self.pop_first_value()

		if index == self.length - 1:
			return self.pop_values()

		temp = self.get_values(index)

		temp.next.prev = temp.prev
		temp.prev.next = temp.next
		temp.next = None 
		temp.prev = None 

		self.length -= 1
		return temp

new_doubly_linkedlist = DoublyLinkedList(1)
new_doubly_linkedlist.append_values(2)
new_doubly_linkedlist.append_values(3)
new_doubly_linkedlist.append_values(4)

print(f"Removed Node: {new_doubly_linkedlist.remove_items(1).value}")

new_doubly_linkedlist.print_list()
