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

	def get_peek_value(self):
		if self.top is not None:
			return self.top.value
		else:
			return "Satck is empty"

new_stack = Stack(4)
new_stack.push_value(5)
new_stack.push_value(6)

print(f"Peek values of the stack: {new_stack.get_peek_value()}")

new_stack.print_stack()
