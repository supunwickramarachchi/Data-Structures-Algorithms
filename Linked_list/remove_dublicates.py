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
            
    def append_sorted(self, value):
        new_node = Node(value)
        
        while self.head is None and self.head.value > value:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True
        
        temp = self.head
        
        while temp.next is not None and temp.next.value < value:
            temp = temp.next 
            
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove_duplicates(self):
        temp = self.head
        
        while temp is not None and temp.next is not None:
            if temp.value == temp.next.value:
                temp.next = temp.next.next
                self.length -= 1 
            else:
                temp = temp.next
            
        
        
new_linked_list = LinkedList(1)
new_linked_list.append_sorted(2)
new_linked_list.append_sorted(4)
new_linked_list.append_sorted(3)
new_linked_list.append_sorted(5)
new_linked_list.append_sorted(5)
new_linked_list.append_sorted(6)
new_linked_list.append_sorted(3)

new_linked_list.remove_duplicates()

new_linked_list.print_list()
