''' The purpose of the Valid Parentheses Check function is to 
determine whether a given string containing various types of 
brackets (e.g., "()", "{}", "[]") is balanced and valid.'''

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
		return None 

	def pop_value(self):
		if self.height ==0:
			return none 

		temp = self.top 

		self.top = self.top.next
		temp.next = None 

		self.height -= 1
		return temp

	def is_valid_parentheses(self, string):
		# Create a stack to hold opening brackets
		stack = []
		# Define the matching pairs in the string 
		matching_pairs = {')':'(', '}':'{', ']':'['}

		# Traverse each character in the string
		for char in string:
			if char in matching_pairs.values(): # If it's an opening bracket
				stack.append(char)
			elif char in matching_pairs.keys(): # If it's a closing bracket
				# If stack is empty or top doesn't match, string is invalid
				if not stack or stack.pop() != matching_pairs[char]:
					return False
		# If stack is empty after traversal, string is valid
		return len(stack) == 0

new_stack = Stack(14)
new_stack.push_value(15)

new_stack.pop_value()

new_stack.print_stack()

print(new_stack.is_valid_parentheses('[{}]'))
