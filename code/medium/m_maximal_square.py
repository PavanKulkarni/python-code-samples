import random

def maximal_square(d):
    if not d:
        return 0

    for i in range(1, len(d)):
        for x in range(1, len(d[i])):
            if d[i][x] == 1:
                # +1 is important here since it propgates the square throuhgout
                d[i][x] = min(d[i][x-1], d[i-1][x], d[i-1][x-1]) + 1
    return max(map(max, d))**2



def print_m(d):
    for i in range(len(d)):
        print d[i]
    print '============'

if __name__=='__main__':
    a = [[random.randint(0,1) for i in range(4)] for x in range(4)]
    print 'TEST1'
    print_m(a)
    print maximal_square(a)

    all_1 = [[1 for i in range(4)] for x in range(4)]
    print 'TEST2'
    print_m(all_1)
    print maximal_square(all_1)

    all_0 = [[0 for i in range(4)] for x in range(4)]
    print 'TEST3'
    print_m(all_0)
    print maximal_square(all_0)