from library.node import Node
from library.linked_list import LinkedList

if __name__=='__main__':
    nn = Node(1)
    ll = LinkedList(nn)
    print '******* Started Linked List ********'
    ll.print_linked_list()

    # Insert
    nn1 = Node(2)
    ll.insert(nn1)
    print '****** After Insertion ********'
    ll.print_linked_list()

    # Delete
    ll.delete(nn)
    print '****** After Deletion *******'
    ll.print_linked_list()

