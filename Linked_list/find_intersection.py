class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 0
        
    def print_list(self):
        temp = self.head 
        
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def get_length(self):
        return self.length
            
    def insert_value_sorted(self, value):
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
    

new_linked_list_1 = LinkedList(0)
new_linked_list_1.insert_value_sorted(1)
new_linked_list_1.insert_value_sorted(2)
new_linked_list_1.insert_value_sorted(3)
new_linked_list_1.insert_value_sorted(4)
new_linked_list_1.insert_value_sorted(5)
new_linked_list_1.insert_value_sorted(6)

new_linked_list_2 = LinkedList(4)
new_linked_list_2.insert_value_sorted(5)
new_linked_list_2.insert_value_sorted(6)
new_linked_list_2.insert_value_sorted(7)

# new_linked_list_1.print_list()
# new_linked_list_2.print_list()


def find_intersection(list_1, list_2):
    len_1 = new_linked_list_1.get_length()
    len_2 = new_linked_list_2.get_length()
    
    difference = abs(len_1 - len_2)
    
    longer, shorter = (list_1.head, list_2.head) if len_1 > len_2 else (list_2.head, list_1.head)
    
    for _ in range(difference):
        longer = longer.next
        
        
    while longer and shorter:
        if longer == shorter:
            return longer
        longer = longer.next
        shorter = shorter.next
        
    return None

print(find_intersection(new_linked_list_1, new_linked_list_2))
