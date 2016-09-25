class BinaryTree(object):
	def __init__(self, content):
		self.content = content
		self.right = None
		self.left = None

	def set_left(self,left):
		self.left = left
 
	def set_right(self,right):
		self.right = right

	def print(self):
		print '%s->' % self.content

def build(i_a):
	if len(i_a) > 3:
		

def buildtree(i_a, p_a):
	# Last element of p_a is the root
	root = BinaryTree(p_a[-1])
	


if __name__='__main__':
	i_a = [4,2,5,1,6,7,3,8]
	p_a = [4,5,2,6,7,8,3,1]
	buildtree(i_a, p_a)
