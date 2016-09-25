import random
import collections
def dup3(nums, k, t):
    if k < 1 or t < 0:
        return False
    cache = collections.OrderedDict()

    for i in range(len(nums)):
        # Put all values into same bucket which is divided by t
        key = nums[i] / max(1, t)

        # since dividing by t can end up with less or greater than by 1 unit.
        for m in (key, key -1, key +1):
            if m in cache and abs(nums[i] - cache[m]) <= t:
                return True

        cache[key] = nums[i]

        if i >= k:
            cache.popitem(last=False)

if __name__=='__main__':
    test = [random.randint(1,10) for i in xrange(10)]
    k = random.randint(1,10)
    print test, k
    print dup3(test, k, 2)
