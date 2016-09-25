class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def find_intersection(headA, headB):
    if headA is None or headB is None:
        return None
    intersection_found = False
    tempA= headA
    tempB = headB
    lastA = None
    lastB = None
    no_intersecting_node = False
    while not intersection_found:
        if tempA.val == tempB.val:
            print 'intersection_found'
            intersection_found = True
        if tempA.next is not None:
            tempA = tempA.next
            print 'A..%s' % tempA.val
        else:
            lastA = tempA
            print 'Switching A to headB'
            tempA = headB
        if tempB.next is not None:
            tempB = tempB.next
            print 'B..%s' % tempB.val
        else:
            lastB = tempB
            print 'Switching B to headA'
            tempB = headA

        if lastA is not None and lastB is not None:
            if lastA.val != lastB.val:
                no_intersecting_node = True
                intersection_found = True

    if no_intersecting_node:
        return None
    return tempA


def _populate(val):
    if len(val) == 1:
        return ListNode(val[0])
    me = ListNode(val[-1])
    me.next = _populate(val[:-1])
    return me

def print_ll(a):
    while a is not  None:
        print '%s->'%a.val
        a = a.next

if __name__=='__main__':
    A = [1,3,5,7,9,11]
    headA = _populate(A[::-1])
    B = [2,4,9,11]
    headB = _populate(B[::-1])
    print_ll(headA)
    print '============='
    print_ll(headB)
    print '============='

    int_node = find_intersection(headA, headB)
    print_ll(int_node)



