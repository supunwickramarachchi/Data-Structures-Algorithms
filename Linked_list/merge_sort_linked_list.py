class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
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
    
    def find_middle_node(self):
        slow = self.head 
        fast = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next 
            
        return 
    
    def merge_sort_list(self, head):
        if not head or not head.next:
            return head
        
        prev = None 
        slow = head 
        fast = head
        
        while fast and fast.next:
            prev = slow 
            slow = slow.next
            fast = fast.next.next
            
        if prev:
            prev.next = None
            
        left = self.merge_sort_list(head)
        right = self.merge_sort_list(slow)
        
        dummy = Node(0)
        tail = dummy
        
        while left and right:
            if left.value < right.value:
                tail.next = left 
                left = left.next 
            else:
                tail.next = right 
                right = right.next 
                
            tail = tail.next
            
        tail.next = left if left else right 
        
        return dummy.next

        
new_linked_list = Linked_list(1)
new_linked_list.append_items(2)
new_linked_list.append_items(3)
new_linked_list.append_items(1)
new_linked_list.append_items(4)
new_linked_list.append_items(3)
new_linked_list.append_items(5)
new_linked_list.append_items(2)

new_linked_list.head = new_linked_list.merge_sort_list(new_linked_list.head)

new_linked_list.print_list()
