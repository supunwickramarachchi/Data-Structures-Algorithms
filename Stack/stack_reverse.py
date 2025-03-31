class Node:
	def __init__(self, value):
		self.value = value
		self.next = None 


class Stack:
	def __init__(self, value):
		new_node = Node(value)
		self.top = new_node
		self.height = 1

	def print_stack(self):
		temp = self.top
		while temp is not None:
			print(temp.value)
			temp = temp.next

	def push_value(self, value):
		new_node = Node(value)

		if self.height == 0:
			self.top = new_node
		else:
			new_node.next = self.top
			self.top = new_node

		self.height += 1
		return True

	def pop_value(self):
		if self.height == 0:
			return None 

		temp = self.top

		self.top = self.top.next
		temp.next = None 

		self.height -= 1
		return temp.value

	def reverse_stack(self):
		if self.height == 0: return None 

		top_element = self.pop_value()
		self.reverse_stack()
		self.insert_at_bottom(top_element)

	def insert_at_bottom(self, value):
		if self.height == 0:
			return self.push_value(value)

		top_value = self.pop_value()
		self.insert_at_bottom(value)
		self.push_value(top_value)


new_stack = Stack(4)
new_stack.push_value(5)
new_stack.push_value(6)
new_stack.push_value(7)
new_stack.push_value(8)

new_stack.reverse_stack()

new_stack.print_stack()
