class Node:
	def __init__(self, value):
		self.value = value
		self.next = None 
		self.prev = None 

class DoublyLinkedList:
	def __init__(self, value):
		new_node = Node(value)
		self.head  = new_node
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

	def is_palindrome(self):
		if self.length <= 1:
			return True

		forward_node = self.head
		backward_node = self.tail 

		for i in range(self.length // 2):
			if forward_node.value != backward_node.value:
				return False

			forward_node, backward_node = forward_node.next, backward_node.prev

		return True


new_doubly_linkedlist = DoublyLinkedList(1)
new_doubly_linkedlist.append_values(2)
new_doubly_linkedlist.append_values(3)
new_doubly_linkedlist.append_values(2)
new_doubly_linkedlist.append_values(1)

new_doubly_linkedlist.print_list()

print(f"Is Palindrome: {new_doubly_linkedlist.is_palindrome()}")
