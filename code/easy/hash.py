class C(object):
    def __hash__(self):
        return 42


class D(C):
    def __eq__(self, other):
        return hash(self) == hash(other)

if __name__ =='__main__':
	c, d = C(), C()
	x = {c: 'c', d: 'd'}
	print x

	p, q = D(), D()
	y = {p:'p', q:'q'}
	print y
