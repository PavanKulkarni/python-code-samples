# Definition for singly-linked list.
import copy
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def swapPairs(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        count = 0
        prev = None
        next = None
        current = head
        while (head is not None and count < 2):
           next = current.next
           current.next = prev
           prev = current
           current = next
           count += 1
        head.next = swapPairs(current) 
        return prev


if __name__=='__main__':
      l1 = ListNode(1)
      l2 = ListNode(2)
      l3 = ListNode(3)
      l4 = ListNode(4)
      l1.next = l2
      l2.next = l3
      l3.next = l4
      ret = swapPairs(l1)        


      nasca, asia capital, lima el capital
