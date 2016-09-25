import random
def dup2(nums, k):
    print nums
    print k
    cache = {}
    n = len(nums)
    if not nums or len(nums) == 1:
        return False
    for i in range(n):
        if nums[i] not in cache:
            cache[nums[i]] = i
        else:
            # hit check the indexes
            if abs(i-cache[nums[i]]) <= k:
                print 'The repeated number is %s' % nums[i]
                return True
            cache[nums[i]] = i
    return False


if __name__=='__main__':
    test = [random.randint(1,10) for i in xrange(10)]
    print dup2(test, random.randint(1,10))
