

def single_number(nums):
    cache = set()
    for i in nums:
        if i not in cache:
            cache.add(i)
        elif i in cache:
            cache.remove(i)
    return list(cache)[0] 	




if __name__=='__main__':
    test = [[1,1,2,2,3], [1,1,2,5,6,5,6]]
    for i in test:
	   print single_number(i)
