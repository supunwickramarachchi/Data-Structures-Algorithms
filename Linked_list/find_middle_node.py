class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 
        
class Linkedlist:
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
        
        if self.head is None or self.head.value >= value:
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
    
    def find_middle(self):
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next 
            
        return slow
    
    
linked_list_1 = Linkedlist(1)
linked_list_1.append_sorted(2)
linked_list_1.append_sorted(4)
linked_list_1.append_sorted(5)
linked_list_1.append_sorted(3)

print("Middle Node: {}".format(linked_list_1.find_middle().value))

linked_list_1.print_list()
