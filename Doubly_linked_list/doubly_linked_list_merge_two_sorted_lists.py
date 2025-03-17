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


new_doubly_linkedlist_1 = DoublyLinkedList(1)
new_doubly_linkedlist_1.append_values(3)
new_doubly_linkedlist_1.append_values(5)


new_doubly_linkedlist_2 = DoublyLinkedList(2)
new_doubly_linkedlist_2.append_values(4)
new_doubly_linkedlist_2.append_values(6)


def merging_two_sorted_list(list_1, list_2):
	dummy = Node(0) # Create a dummy node start a merged list
	tail = dummy # Use tail to build the new list frommthe dummy

	current_1 = list_1.head # Pointer to the head of the first list
	current_2 = list_2.head # pointer to the head of the second list

	while current_1 and current_2: # While both lists are not empty
		if current_1.value < current_2.value: # Compare the current nodes
			tail.next = current_1 # Attach the smaller node
			current_1.prev = tail # Update the preview pointer
			current_1 = current_1.next # Move to the next node of the first list
		else:
			tail.next = current_2 # Attach the smaller node 
			current_2.prev = tail # Update the preview pointer
			current_2 = current_2.next # Move to the next node of the second list

		tail = tail.next # Move the tail to the newly added node

	# Attaching remaining nodes from either list
	if current_1: # If there are remaining nodes in the first list
		tail.next = current_1
		current_1.prev = tail
	else: # Aif there are remaining nodes in the second list
		tail.next = current_2
		if current_2: 
			current_2.prev = tail 

	return dummy.next # Return the head of the merged list (dummy.next)
  

def merging_two_sorted_list(list_1, list_2):
	dummy = Node(0)
	tail = dummy

	current_1 = list_1.head
	current_2 = list_2.head

	while current_1 and current_2:
		if current_1.value < current_2.value:
			tail.next = current_1
			current_1.prev = tail 
			current_1 = current_1.next
		else:
			tail.next = current_2
			current_2.prev = tail 
			current_2 = current_2.next

		tail = tail.next

	if current_1:
		tail.next = current_1
		current_1.prev = tail
	else:
		tail.next = current_2
		if current_2:
			current_2.prev = tail

	return dummy.next

merge_list = merging_two_sorted_list(new_doubly_linkedlist_1, new_doubly_linkedlist_2)

print(merge_list.value)

