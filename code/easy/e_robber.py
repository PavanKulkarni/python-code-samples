
import random
# Important thing is that the max is max(last number of current + (last -2))
def robber(nums):
    n = len(nums)
    dp = [0]*(n+1)
    if n >0:
        dp[1] = nums[0]

    for i in range(2, n+1):
        dp[i] =  max(dp[i-1], dp[i-2] + nums[i-1])

    return dp[n]



if __name__=='__main__':
    test = [random.randint(1, 10) for i in range(10)]
    print test
    print robber(test)
