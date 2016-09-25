class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def add_ll(l1, l2):
    carry = 0
    sum = 0
    l3 = None
    head = None
    while (l1 is not None or l2 is not None):
        tmp_sum = int(l1.val) + int(l2.val) + carry
        import pdb;pdb.set_trace()
        if tmp_sum >= 10:
            sum = tmp_sum % 10
            carry = 1
        else:
            sum = tmp_sum
        tmp_node = ListNode(sum)
        if l3 is None:
            l3 = tmp_node
            head = l3
        else:
            l3.next = tmp_node
            l3 = l3.next
        if l1.next is None:
            while l2.next is not None:
                l2 = l2.next
                l3.next = ListNode(l2.val)
                l3 = l3.next
        else:
            l1 = l1.next
        if l2.next is None:
            while l1.next is not None:
                l1 = l1.next
                l3.next = ListNode(l1.val)
                l3 = l3.next
        else:
            l2 = l2.next

    return head


def construct_number(n):
    num_list = list(str(n))
    prev = None
    head = None
    for i in reversed(xrange(len(num_list))):
        current = ListNode(num_list[i])
        if prev is not None:
            prev.next = current
        else:
            head = current
        prev = current

    return head


def print_ll(l):
    if l is None:
        return
    while l.next is not None:
        print '%s->' % l.val
        l = l.next
    print '%s->' %l.val

if __name__=='__main__':
    l1 = construct_number(342)
    # print_ll(l1)
    l2 = construct_number(465)
    # print_ll(l2)
    l3 = add_ll(l1, l2)
    print_ll(l3)
