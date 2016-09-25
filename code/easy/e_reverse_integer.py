

def rev_int_naive(n):
    str_int = list(str(n))
    x = 0
    y = len(str_int) -1
    rev_int = ''
    while x < y:
        str_int[x], str_int[y] = str_int[y], str_int[x]
        x += 1
        y -= 1
    return int(''.join(str_int))

def rev_int_effiecient(x):
    flag = False
    if x < 0:
        x = 0 - x
        flag = true
 
    res = 0
    p = x
    while p > 0:
        mod = p % 10
        p = p / 10
        res = res * 10 + mod
 
    if flag:
        res = 0 - res
 
    return res;

if __name__=='__main__':
    print rev_int_naive(12399)
    print rev_int_effiecient(12399)
