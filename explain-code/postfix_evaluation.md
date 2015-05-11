1. I had worked on a lot of python code, but had never started a project from scratch, and hence some learnings from it.
* Put __init__.py in the directory you want to be considered as modules and import them in other places of your python code.
* Append the main directory of the project to PYTHONPATH. This can be in ~/.bashrc or can be done only for session.
* To reload bashrc after the changes I used source and learnt that source in bash basically executes anything in the file passed as argument to it Ex: source ~/.bashrc
* Learnt to use optparse for parsing the command-line arguments.

-- POSTFIX Evaluation --
* A Postfix traversal is traversing a tree, as left node -> right node -> root node.
* Any mathematical expression can be expressed as postfix expression where left and right nodes are operands and root nodes are operators.
* The logic is start evaluating the expression, and when you encounter operands put them in stack and when you encounter operator, pop two operands from stack and apply the operator on them
and store the result back in the stack.
* The final result in the stack should the final result of the mathematical expression.

