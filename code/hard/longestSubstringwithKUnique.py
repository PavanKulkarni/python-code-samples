
def klongest(test, k):
	longest_string = 0
	unique_reset_counter = False
	per_char_counter = 0
	last_char = k[0]
	for char in test:
		if char == last_chart and unique_reset_counter:
			per_char_counter += 1
		else:
			unique_reset_counter = True




if __name__=='__main__':
	test_strings = ['aabb', 'aabbcc', 'abc', 'abbbccd']
	for i in test_strings:
		klongest(i,1)
