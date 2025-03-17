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
			self.head  = new_node
			self.tail = new_node

		else:
			self.tail.next = new_node
			new_node.prev = self.tail
			self.tail = new_node

		self.length += 1
		return True

	def pop_items(self):
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

	def pop_items(self):
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


new_doubly_linkedlist = DoublyLinkedList(0)
new_doubly_linkedlist.append_items(1)
new_doubly_linkedlist.append_items(2)
new_doubly_linkedlist.append_items(3)
new_doubly_linkedlist.append_items(4)


new_doubly_linkedlist.print_list()

print("After Deletion")

# (5) Items - only have 4 nodes
print(new_doubly_linkedlist.pop_items().value)
# (4) Items - only have 3 nodes
print(new_doubly_linkedlist.pop_items().value)
# (3) Items - only have 2 nodes
print(new_doubly_linkedlist.pop_items().value)
# (2) Items - only have 1 nodes
print(new_doubly_linkedlist.pop_items().value)
# (1) Items - only have 0 nodes
print(new_doubly_linkedlist.pop_items().value)
# (0) Items - None nodes
print(new_doubly_linkedlist.pop_items())

new_doubly_linkedlist.print_list()

