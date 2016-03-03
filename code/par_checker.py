from library.stack import Stack

def parChecker(symbolString):
    ll = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
	symbol = symbolString[index]
	if symbol == '(':
	   ll.push(symbol)
	else:
	   if ll.isEmpty():
		balanced = False
	   else:
		ll.pop()
        index += 1

    if balanced and ll.isEmpty():
        return True
    else:
	return False

if __name__=='__main__':
   print parChecker('(())')
   print parChecker('(())(())')
   print parChecker('()()()()((()))')
   print parChecker('(()(()(())((()((')


