class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 
        
class LinkedList:
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
            
    def append_items(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return True 
        
    def reverse_linked_list(self, head):
        prev = None 
        current = head 
        
        while current:
            next_temp = current.next 
            current.next = prev
            prev = current
            current = next_temp
            
        return prev
        
    def is_palindrome(self):
        # Edge cases
        if not self.head or not self.head.next:
            return True
        
        # Find the middle node
        slow = fast = self.head 
        
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next 
            
        # Reverse the second half
        second_half = self.reverse_linked_list(slow.next)
        
        first_half = self.head 
        
        while second_half:
            if first_half.value != second_half.value:
                return False
            first_half = first_half.next 
            second_half = second_half.next 
            
        return True
        
        
new_linked_list = LinkedList(1)
new_linked_list.append_items(2)
new_linked_list.append_items(3)
new_linked_list.append_items(3)
new_linked_list.append_items(2)
new_linked_list.append_items(1)

new_linked_list.print_list()

print(f"Is this list palindrome: {new_linked_list.is_palindrome()}")

