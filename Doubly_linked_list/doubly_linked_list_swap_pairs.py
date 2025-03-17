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

	def swap_pairs(self):
		dummy = Node(0)
		dummy.next = self.head
		prev = dummy

		while self.head and self.head.next:
			fisrt_node, second_node = self.head, self.head.next

			prev.next = second_node
			fisrt_node.next = second_node.next
			second_node.next = fisrt_node

			second_node.prev = prev
			fisrt_node.prev = second_node

			# If the next node (first_node.next) exists, update its prev pointer 
			# to correctly point back to first_node, maintaining the DLL structure.
			if fisrt_node.next:
			    fisrt_node.next.prev = fisrt_node


			self.head = fisrt_node.next # Move to next node  for swaping
			prev = fisrt_node # set prev to first node from dummy
		
		self.head = dummy.next # After swap bring the head to the correct position


new_doubly_linkedlist = DoublyLinkedList(1)
new_doubly_linkedlist.append_values(2)
new_doubly_linkedlist.append_values(3)
new_doubly_linkedlist.append_values(4)
new_doubly_linkedlist.append_values(5)

new_doubly_linkedlist.swap_pairs()

new_doubly_linkedlist.print_list()
