class Node:
	def __init__(self, value):
		self.value = value
		self.next = None 

class Stack:
	def __init__(self, value, max_size):
		new_node = Node(value)
		self.top = new_node
		self.height = 1 
		self.max_size = max_size

	def print_stack(self):
		temp = self.top 

		while temp is not None:
			print(temp.value)
			temp = temp.next

	def push_value(self, value):
		if self.height == self.max_size:
			return 'Stack overflow! Cannot push more elements.'

		new_node = Node(value)

		new_node.next = self.top
		self.top = new_node
		self.height += 1
		return f"Pushed {value} onto the stack"


new_stack = Stack(4, 5)
new_stack.push_value(5)
new_stack.push_value(6)
new_stack.push_value(7)
new_stack.push_value(8)
print(new_stack.push_value(10))

new_stack.print_stack()
