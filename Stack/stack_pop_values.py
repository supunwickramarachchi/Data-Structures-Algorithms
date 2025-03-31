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

	def pop_values(self):
		if self.height == 0:
			return None 

		temp = self.top

		self.top = self.top.next
		temp.next = None

		self.height -= 1 
		return temp


new_stack = Stack(4)
new_stack.push_value(3)
new_stack.push_value(5)
new_stack.push_value(2)

print(f"Removed Value: {new_stack.pop_values().value}")
print(f"Removed Value: {new_stack.pop_values().value}")
print(f"Removed Value: {new_stack.pop_values().value}")

new_stack.print_stack()
