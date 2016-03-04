from library.stack import Stack

def matches(open,close):
    openers = '({['
    closers = ')}]'
    return openers.index(open) == closers.index(close)

def parChecker(symbolString):
    ll = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
	symbol = symbolString[index]
	if symbol in '({[':
	   ll.push(symbol)
	else:
	   if ll.isEmpty():
		balanced = False
	   else:
                open = ll.pop()
		if not matches(open, symbol):
		    balanced = False
		   
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
   print parChecker('{{()}}')
   print parChecker('[{{}}([])]')
   print parChecker('{{{][][][]())))')


