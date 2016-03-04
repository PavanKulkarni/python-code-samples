from library.stack import Stack

def binary(decimal_num):
   stack = Stack()
   while decimal_num > 0:
	rem = decimal_num %2
        stack.push(rem)
        decimal_num = int(decimal_num / 2)

   binary_num = ""
   while not stack.isEmpty():
        binary_num = '%s%s' %(binary_num,stack.pop())
   
   return binary_num


if __name__=='__main__':
   print '20 in binary is %s' % binary(20)
   print '5 in binary is %s' % binary(5)
   print '1212 in binary is %s' % binary(1212)
   print '7 in binary is %s' % binary(7)


