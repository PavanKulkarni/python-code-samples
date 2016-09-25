

def cs(candidates, target):
    candidates.sort()
    res = []
    line = []
    helper(candidates, target, res, line)
    return res


def helper(candidates, target, res, line):
    if target == 0:
       res.append([x for x in line])
       return

    for i, x in enumerate(candidates):
      if x <= target:
         line.append(x)
         helper(candidates[i:], target - x, res, line)
         line.pop()




if __name__=='__main__':
	print cs([2,2,3,1,2,3,4], 7)
