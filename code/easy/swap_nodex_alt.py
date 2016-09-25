# Definition for singly-linked list.
import copy
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def swapPairs(head, k, switch):
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
        if switch:
          while (head is not None and count < k):
             next = current.next
             current.next = prev
             prev = current
             current = next
             count += 1
          head.next = swapPairs(current, k , False)
          return prev
        else:
          i = 0
          while i < k:
             current = current.next
             i +=1
          current.next = swapPairs(current, k , True)
          return head



if __name__=='__main__':
      l1 = ListNode(1)
      l2 = ListNode(2)
      l3 = ListNode(3)
      l4 = ListNode(4)
      l5 = ListNode(5)
      l6 = ListNode(6)
      l7 = ListNode(7)
      l1.next = l2
      l2.next = l3
      l3.next = l4
      l4.next = l5
      l5.next = l6
      l6.next = l7
      ret = swapPairs(l1, 3, True)  
      while (ret.next is not None):
          print ret.val 
          ret = ret.next
