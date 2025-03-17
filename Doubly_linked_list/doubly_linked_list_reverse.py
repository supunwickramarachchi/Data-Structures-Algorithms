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

	def append_items(self, value):
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

	def reverse_list(self):
		temp = self.head 

		while temp is not None:
			temp.prev, temp.next = temp.next, temp.prev
			temp = temp.prev

		self.head, self.tail = self.tail, self.head
		return True


new_doubly_linkedlist = DoublyLinkedList(1)
new_doubly_linkedlist.append_items(2)
new_doubly_linkedlist.append_items(3)
new_doubly_linkedlist.append_items(4)
new_doubly_linkedlist.append_items(5)

new_doubly_linkedlist.reverse_list()

new_doubly_linkedlist.print_list()
