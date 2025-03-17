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

		return True

	def insertion_sort_DLL(self):
		if not self.head:
			return None 

		sorted_head = self.head
		current = self.head.next 
		sorted_head.next = None 

		while current:
			next_node = current.next 
			current.next = None 

			if current.value < sorted_head.value:
				current.next = sorted_head
				sorted_head.prev = current
				sorted_head = current

			else:
				search = sorted_head

				while search.next and search.next.value < current.value:
					search = search.next 

				current.next = search.next 
				if search.next:
					search.next.prev = current
				current.prev = search
				search.next = current

			current = next_node

		return sorted_head


new_doubly_linkedlist = DoublyLinkedList(1)
new_doubly_linkedlist.append_values(5)
new_doubly_linkedlist.append_values(2)
new_doubly_linkedlist.append_values(4)
new_doubly_linkedlist.append_values(3)

print("The list before sort: ")
new_doubly_linkedlist.print_list()
print()

new_doubly_linkedlist.insertion_sort_DLL()

print("The list after sort: ")
new_doubly_linkedlist.print_list()

