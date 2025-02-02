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
    
    def  prepend_items(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def get_items(self, index):
        if index < 0 or index >= self.length:
            return None 
        temp = self.head 
        
        for _ in range(self.length):
            temp = temp.next 
        return temp
    
    def pop_value(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        
        while temp.next:
            pre = temp
            temp = temp.next
            
        self.tail = pre
        self.tail.next = None 
        self.length -= 1
        
        if self.length == 0:
            self.head = None 
            self.tail = None
        return temp
    
    def pop_first_value(self):
        if self.length == 0:
            return None 
        
        temp = self.head
        self.head = self.head.next
        temp.next = None 
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def remove_items(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first_items()
        if index == self.length - 1:
            return self.pop_items()
        
        pre = self.get_items(index - 1)
        temp = pre.next 
        pre.next = temp.next
        temp.next = None 
        self.length -= 1
        return temp
        
            
    def reverse_list(self):
        temp = self.head
        self.head = self.tail 
        self.tail = temp
        after = temp.next 
        before = None
        
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after 
            

new_linked_list = LinkedList(1)
new_linked_list.append_items(2)
new_linked_list.append_items(3)
new_linked_list.append_items(4)
new_linked_list.append_items(5)
new_linked_list.append_items(6)
new_linked_list.prepend_items(0)

new_linked_list.reverse_list()

new_linked_list.print_list()
