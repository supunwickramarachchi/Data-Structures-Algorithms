def infix_to_postfix(expression):
    # Define operator precedence in a dictionary
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}  # Higher numbers = higher priority
    stack = []  # Stack to hold operators temporarily
    postfix = []  # Resulting postfix expression (list to build the string)

    # Traverse the infix expression character by character
    for char in expression:
        if char.isalnum():  # If it's an operand (letters A-Z or digits 0-9)
            postfix.append(char)  # Add directly to the postfix expression
        elif char == '(':  # If it's a left parenthesis
            stack.append(char)  # Push '(' onto the stack
        elif char == ')':  # If it's a right parenthesis
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())  # Pop operators until '('
            stack.pop()  # Remove '(' itself from the stack
        else:  # If it's an operator (+, -, *, /)
            while stack and precedence[stack[-1]] >= precedence[char]:
                postfix.append(stack.pop())  # Pop higher precedence operators to postfix
            stack.append(char)  # Push the current operator onto the stack

    # After the expression is traversed, pop any remaining operators from the stack
    while stack:
        postfix.append(stack.pop())

    # Join the list into a single string and return the postfix expression
    return ''.join(postfix)

# Example usage
expression = "(A+B)*C"
print("Postfix Expression:", infix_to_postfix(expression))  # Output: AB+C*
