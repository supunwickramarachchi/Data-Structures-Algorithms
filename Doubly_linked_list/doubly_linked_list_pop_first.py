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


	def append_value(self, value):
		new_node = Node(value)

		if self.length == 0:
			self.head = new_node
			self.tail = new_node

		else:
			self.tail.next = new_node
			new_node.prev = self.tail
			self.tail = new_node

		self.length += 1
		return True


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

new_doubly_linkedlist = DoublyLinkedList(1)
new_doubly_linkedlist.append_value(2)
new_doubly_linkedlist.append_value(3)
new_doubly_linkedlist.append_value(4)
new_doubly_linkedlist.append_value(5)

new_doubly_linkedlist.pop_first_value()

new_doubly_linkedlist.print_list()


