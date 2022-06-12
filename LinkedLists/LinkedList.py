def main():
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)


    # Test get_position
    # Should print 3
    print(ll.head.next.next.value)
    # Should also print 3
    print(ll.get_position(3).value)

    # Test insert
    ll.insert(e4,3)
    # Should print 4 now
    print(ll.get_position(3).value)

    # Test delete
    ll.delete(1)
    # Should print 2 now
    print(ll.get_position(1).value)
    # Should print 4 now
    print(ll.get_position(2).value)
    # Should print 3 now
    print(ll.get_position(3).value)




class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        
        if self.head:
            if position == 1:
                return self.head
            else:
                current = self.head
                for i in range(1, position):
                    if not current.next: return None
                    current = current.next
                return current
        else:
            return None
            
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if self.head is None:
            raise Exception("List is empty.")
            
        current = self.head
        pointer = 1
        
        while pointer != position:
            
            if current.next is None:
                raise Exception("Given position out of bounds.")
                
            prev = current
            current = current.next
            pointer += 1
            if pointer == position:
                prev.next = new_element
                new_element.next = current
                return
                
    
    def delete(self, value):
        """Delete the first node with a given value."""
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.value == value:
            self.head = self.head.next
            return
        
        previous_node = self.head
        for node in self:
            if node.value == value:
                previous_node.next = node.next
                return
            previous_node = node
            
        raise Exception(f"Node with value {value} not found.")


if __name__ == "__main__":
    main()