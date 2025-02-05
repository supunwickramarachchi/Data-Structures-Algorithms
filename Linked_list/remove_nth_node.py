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
        new_node  = Node(value)
        
        while self.head is None and self.head.value >= value:
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

    def get_items(self, index):
        if index < 0 or index >= self.length:
            return None 
        
        temp = self.head
        
        for _ in range(index):
            temp = temp.next 
            
        return temp
    
    def pop_items(self):
        if self.head is None:
            return None 
        
        temp = self.head
        pre = self.head
        
        while temp.next:
            pre = temp
            temp = temp.next
            
        self.tail = pre
        pre.next = None 
        self.length -= 1
        
        while self.length == 0:
            self.head = None 
            self.tail = None 
            
        return temp
            
    def pop_first_item(self):
        if self.length == 0:
            return None 
        
        temp = self.head
        self.head = self.head.next
        temp.next = None 
        self.length -= 1
        
        while self.length == 0:
            self.tail = None 
        return temp 
    
    def remove_items(self, index):
        if index < 0 or index >= self.length:
            return None 
        
        if index == 0:
            return self.pop_first_item()
        
        if index == self.length - 1:
            return self.pop_items()
        
        temp = self.head
        
        for _ in range(index):
            temp = temp.next
            
        pre = self.get_items(index - 1)
        temp = pre.next 
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
        
        
    
    def remove_nth_node(self, nth_node):
        
        if nth_node < 0 or nth_node >= self.length:
            return None
            
        if nth_node == 0:
            return self.pop_first_item()
        
        if nth_node == self.length - 1:
            return self.pop_items()
        
        temp = self.head 
        
        for _ in range(self.length - nth_node - 1):
            temp = temp.next 
            
        pre = temp
        temp = temp.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        
        if self.length == 0:
            self.tail = None
        return temp
    
    
    
new_linked_list = Linkedlist(1)
new_linked_list.append_sorted(3)
new_linked_list.append_sorted(2)
new_linked_list.append_sorted(4)
new_linked_list.append_sorted(5)
new_linked_list.append_sorted(6)
            
new_linked_list.print_list()

print("nth node: ", new_linked_list.remove_nth_node(3).value)

print("After removing nth node")

new_linked_list.print_list()
