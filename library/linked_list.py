class LinkedList():

    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def size(self):
        return self.size

    def insert(self, node):
        if not self.head:
            self.head = node
        else:
            # set new node's next to current head
            node.next = self.head
            # change head to point to current node
            self.head = node
        self.size += 1

    def delete(self, node):
        if not self.size:
            raise ValueError('Linked List is Empty')
        else:
            current = self.head
            previous = None
            found = False
            while not found:
                if current == node:
                    found = True
                elif current is None:
                    raise ValueError('This node is not in Linked List')
                else:
                    previous = current
                    current = current.next

            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next
            self.size -= 1
        
    def print_linked_list(self):
        if self.head:
           temp  = self.head
           print temp.value
           while temp.next is not None:
               temp = temp.next
               print temp.value

        
