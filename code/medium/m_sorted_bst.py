import math
import random
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sorted_bst(a):
    if not a:
        return None
    return _helper(a)

def _helper(a):
    if not a:
        return None
    if len(a) == 1:
        return TreeNode(a[0])
    mid = int(math.floor(len(a)/2))
    current = TreeNode(a[mid])
    current.left = _helper(a[0:mid])
    current.right = _helper(a[mid+1:len(a)])
    return current

def print_bst(a, marker = 'root'):
    if a is None:
        return
    print 'I am %s:%s' % (marker, a.val)
    print_bst(a.left, 'left')
    print_bst(a.right, 'right')


if __name__=='__main__':
    test = sorted([random.randint(1,10) for i in xrange(10)])
    ret_val = sorted_bst(test)
    print test
    print_bst(ret_val)
