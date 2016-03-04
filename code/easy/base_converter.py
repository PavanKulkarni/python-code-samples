from library.stack import Stack

def base_converter(number, base):
   digits = "0123456789ABCDEF"
   stack = Stack()
   while number > 0:
	rem = number % base
        stack.push(rem)
        number = int(number / base)

   converted_num = ""
   while not stack.isEmpty():
        converted_num = '%s%s' %(converted_num, digits[stack.pop()])
   
   return converted_num


if __name__=='__main__':
   print 'DEC to BINARY'
   print '20 in binary is %s' % base_converter(20, 2)
   print '5 in binary is %s' % base_converter(5, 2)
   print '1212 in binary is %s' % base_converter(1212, 2)
   print '7 in binary is %s' % base_converter(7, 2)

   print "DEC to OCTAL"
   print '20 in octal is %s' % base_converter(20, 8)
   print '5 in octal is %s' % base_converter(5, 8)
   print '1212 in octal is %s' % base_converter(1212, 8)
   print '7 in octal is %s' % base_converter(7, 8)

   print "DEC TO HEX"
   print '20 in hex is %s' % base_converter(20, 16)
   print '5 in hex is %s' % base_converter(5, 16)
   print '1212 in hex is %s' % base_converter(1212, 16)
   print '7 in hex is %s' % base_converter(7, 16)
