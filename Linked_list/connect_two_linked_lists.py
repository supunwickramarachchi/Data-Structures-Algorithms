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

    def append_items_sorted(self, value):
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
        
    
def merge_sorted_list(list1, list2):
    
    list1 = list1.head
    list2 = list2.head
    
    dummy = Node(0)
    current = dummy
    
    while list1 and list2:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next 
        current = current.next
        
    if list1:
        current.next = list1
    else:
        current.next = list2
        
    return dummy.next
    
    
linked_list_1 = LinkedList(12)
linked_list_1.append_items_sorted(15)
linked_list_1.append_items_sorted(10)
linked_list_1.append_items_sorted(5)

linked_list_2 = LinkedList(3)
linked_list_2.append_items_sorted(1)
linked_list_2.append_items_sorted(4)
linked_list_2.append_items_sorted(2)



print("Linked List 01")
linked_list_1.print_list()

print("Linked List 02")
linked_list_2.print_list()

print("Connected Linked List")

merge_list = merge_sorted_list(linked_list_1, linked_list_2)

temp = merge_list

while temp:
    print(temp.value, end= ' -> ')
    temp = temp.next
    

