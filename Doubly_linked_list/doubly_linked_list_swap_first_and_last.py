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
			new_node.pre = self.tail
			self.tail = new_node

		self.length += 1
		return True

	def swap_first_last(self):
		if self.head is None or self.head == self.tail:
			return None 

		self.head.value, self.tail.value = self.tail.value, self.head.value
		return True


new_doubly_linkedlist = DoublyLinkedList(1)
new_doubly_linkedlist.append_values(2)
new_doubly_linkedlist.append_values(3)
new_doubly_linkedlist.append_values(4)
new_doubly_linkedlist.append_values(5)

new_doubly_linkedlist.swap_first_last()

new_doubly_linkedlist.print_list()
