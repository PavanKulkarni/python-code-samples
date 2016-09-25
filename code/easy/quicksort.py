import random

def partition(a, start, end):
	pivot = a[start]
	left = start + 1
	right = end
	done = False
	while not done:
		while left<= right and a[left] <= pivot:
			left += 1
		while right>= left and a[right] >= pivot:
			right -= 1
		if right < left:
			done = True
		else:
			print 'Swapping %s with %s' % (a[left], a[right])
			a[left], a[right] = a[right], a[left]
		
	# Switch the final places for the pivot point
	a[start], a[right] = a[right], a[start]
	print 'After final pivot swap %s' %a
	return right

# we need quickselect to find medians in unsorted arrays
def quickselect(a, start, end, k):
	found = False
	while not found:
		pivot = partition(a, start, end)
		print 'Pivot is %s' %pivot
		if len(a[start:pivot]) == k:
			return a[start:pivot]
		if len(a[start:pivot]) > k:
			pivot = partition(a, start, pivot)
		else:
			pivot = partition(a, pivot+1, end)

def quicksort(a, start, end):
	if start < end:
		pivot = partition(a, start, end)
		quicksort(a, start, pivot - 1)
		quicksort(a, pivot+1, end)
	return a

if  __name__=='__main__':
	b = [random.randint(1, 100) for i in xrange(10)]
	print b
	print quicksort(b,0, len(b)-1)
	# print quickselect(b,0,len(b)-1, 3)
