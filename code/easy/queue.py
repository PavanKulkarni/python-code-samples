class Queue():

	def __init__(self, capacity):
		self.capacity = capacity
		self.items = []

	def enqueue(self, item):
		if len(self.items) > self.capacity:
			print "Over capacity"
			return
		self.items.insert(0, item)
		print self.items

	def dequeue(self):
		return self.items.pop()	

	




if __name__=='__main__':
	q = Queue(2)
	print q.enqueue(1)
	print q.enqueue(2)
	print q.dequeue()
