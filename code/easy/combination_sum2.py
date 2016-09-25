

def cs(candidates, target):
    candidates.sort()
    res = []
    line = []
    helper(candidates, target, res, line)
    return res


def helper(c,t,res,line):
    if t == 0:
       res.append([x for x in line])
       return

    for i,x in enumerate(c):
      if i > 0 and c[i] == c[i-1]:
          continue
      if x <= t:
         line.append(x)
         helper(c[i+1:], t - x, res, line)
         line.pop()




if __name__=='__main__':
	print cs([2,2,3,1,2,3,4], 7)
