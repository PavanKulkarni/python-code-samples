class Heap(object):

	def __init__(self):
		self.heap_array = [0]

	def push(self, value):
		self.heap_array.append(value)
		print 'Appending value to Heap %s ' % self.heap_array
		self.__bubbleUp(len(self.heap_array) - 1)

	def pop(self):
		# Exchange Root with last
		self.__swap(self.heap_array[0], self.heap_array[-1])
		pop_element = self.heap_array[-1]
		del self.heap_array[-1]
		self.__flushDown(0)
		return pop_element
		

	def __flushDown(self, index):
		if (2*index) > len(self.heap_array):
			# No child
			return
		current = index
		left_child = 2*index
		right_child = 2*index + 1
		swap_index = None
		if self.heap_array[current] < self.heap_array[left_child]:
			swap_index = left_child
		if self.heap_array[current] < self.heap_array[right_child] and self.heap_array[right_child] > self.heap_array[swap_index]:
			swap_index = right_child
		if swap_index is None:
			# The node is at correct position
			return
		self.__swap(self.heap_array[current], self.heap_array[swap_index])
		self.__flushDown(swap_index)

	def __bubbleUp(self, index):
		current = index
		if index == 1:
			# I am root so return
			return
		parent = index/2
		if self.heap_array[current] > self.heap_array[parent]:
			self.__swap(self.heap_array[current], self.heap_array[parent])
			self.__bubbleUp(parent)
		return

	def __swap(self, e1, e2):
		e1, e2 = e2, e1
		
	def printHeap(self, index):
		if index > len(self.heap_array) -1:
			print 'Index passed is big'
			return
		print self.heap_array[index]
		self.printHeap(2*index)
		self.printHeap(2*index + 1)

if __name__=='__main__':
	h = Heap()
	h.push(1)
	h.push(2)
	h.push(3)
	h.printHeap(0)

