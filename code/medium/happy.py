

def happy(n):
	hist = set()
	res = 0
	while 1:
		if n ==	1:
			return True
		while n > 0:
			res += (n%10) * (n%10)
			n = n /10
		if res in hist:
			return False
		else:
			print res
			hist.add(res)
			n = res
			res = 0


if __name__=='__main__':
	print happy(19)
