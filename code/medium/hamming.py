

def hammingdistance( a, b , bits = 32):
    a_int = 0
    for i in a:
        a_int = a_int + ord(i)
    b_int = 0
    for i in b:
        b_int = b_int*10 + ord(i)
    def _hamdist(x, bits): 
        if bits: 
            return (x & 1) + _hamdist(x >> 1, bits-1) 
        return x & 1 
    return _hamdist( a_int ^ b_int, bits) 
	

if __name__=='__main__':
	print hammingdistance(,'bbc')
