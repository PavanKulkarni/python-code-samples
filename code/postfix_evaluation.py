from library.stack import Stack
from optparse import OptionParser

def evaluate_postfix(expression):
    s = Stack()
    operand_list = ['+', '-', '*' , '/']
    for item  in expression:
        if item.lower().isdigit():
            # Item is operand, hence push in stack
            s.push(item)
        elif item in operand_list:
            op1 = op2 = None
            # Item is operator, hence pop two and apply operator on them, and push the result back.
            if not s.isEmpty():
               op2 = s.pop()
            if not s.isEmpty():
               op1 = s.pop()
            if not op1 or not op2:
               return None
            print '**** Evaluating %s %s %s  ***' % (op1, item, op2)
            result = eval(op1 + item + op2)
            s.push(str(result))
    return s.pop()

if __name__=='__main__':
    parser = OptionParser()
    
    # File with all the postfix expressions.
    parser.add_option("-f", "--file", dest="filename",
                      help="FILE to read postfix expressions from", metavar="FILE")
 
    parser.add_option("-e", "--expression", dest="expression",
                      help="provide the postfix expression in quotes")


    (options, args) = parser.parse_args()
    expression = options.expression
    if expression:
        final_result = evaluate_postfix(expression)
        if final_result is not None:
            print "Final result of the expression is: %s" % final_result
        else:
            print "Expression passed is not a valid postfix expression"



