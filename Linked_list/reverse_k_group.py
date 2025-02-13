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
            
    def insert_value(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def reverse_k_group(self, k):
        if not self.head or k == 1:
            return 
        
        # Count nodes
        count = 0
        current = self.head
        while current:
            count +=  1
            current = current.next
            
        print(f"Total Nodes: {count}")
        
        # Create dummy node
        dummy = Node(0)
        dummy.next = self.head
        previous = dummy 
        
        while count >= k:
            current = previous.next
            next_node = current.next
            
            print(f"Reversing Nodes: {current.value} and {next_node.value}")
            
            for i in range(k - 1):
                # Step 1: current points to node after next_node
                current.next = next_node.next
                # Step 2: next_node points to current groups's first node
                next_node.next = previous.next
                # Step 3: previous points to next_node (new first node)
                previous.next = next_node
                # Step 4: prepare for next iteration
                next_node = current.next 
                
            print("After Reversal:")
            self.print_list()
            
            previous = current
            count -= k
            
        self.head = dummy.next 
        

new_linkedlist = LinkedList(1)
new_linkedlist.insert_value(2)
new_linkedlist.insert_value(3)
new_linkedlist.insert_value(4)
new_linkedlist.insert_value(5)

new_linkedlist.reverse_k_group(3)

print("Complete Linked List After Reversal")

new_linkedlist.print_list()
    
