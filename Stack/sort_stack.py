class Node:
	def __init__(self, value):
		self.value = value
		self.next = None 

class Stack:
	def __init__(self, value=None):
		if value is not None:
			new_node = Node(value)
			self.top = new_node
			self.height = 1
		else:
			self.top = None 
			self.height = 0


	def print_stack(self):
		temp = self.top

		while temp is not None:
			print(temp.value)
			temp = temp.next

	def push_stack_value(self, value):
		new_node = Node(value)

		if self.height == 0:
			self.top = new_node	
		else:
			new_node.next = self.top
			self.top = new_node

		self.height += 1
		return True

	def pop_stack_value(self):
		if self.height == 0:
			return None 

		temp = self.top 

		self.top = self.top.next 
		temp.next = None 

		self.height -= 1
		return temp.value

	def sort_stack_value(self):
		temp_stack = Stack()

		while self.height > 0:
			current = self.pop_stack_value()

			while temp_stack.height > 0 and temp_stack.top.value > current:
				self.push_stack_value(temp_stack.pop_stack_value())

			temp_stack.push_stack_value(current)

		while temp_stack.height > 0:
			self.push_stack_value(temp_stack.pop_stack_value())


new_stack = Stack(4)
new_stack.push_stack_value(2)
new_stack.push_stack_value(5)
new_stack.push_stack_value(1)
new_stack.push_stack_value(3)

print('The Stack before the sort')
new_stack.print_stack() 

print('The Stack after the sort')
new_stack.sort_stack_value()
new_stack.print_stack()
