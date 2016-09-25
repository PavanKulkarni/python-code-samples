def word_break(s, wordDict):
        if not s and not wordDict:
            return True
        if not wordDict:
            return False
        if len(s) == 1 and s not in wordDict:
            return False
        DP = [[] for i in range(len(s)+1)]
        DP[0] = [0]
        for i in range(1, len(s)+1):
            for k in range(i+1):
                if DP[k] and s[k:i] in wordDict:
                    DP[i].append(k)

        res = []
        print "DP is %s" % DP
        backtrack(DP, s, len(s), res, '')
        return res

def backtrack(dp, s, idx, res, line):
    for i in dp[idx]:
          newline = s[i:idx] + ' ' + line if line else s[i:idx]
          if i == 0:
               res.append(newline)
          else:
               backtrack(dp, s, i, res, newline)



if __name__=='__main__':
     s = "catsanddogs"
     wordDict = ("cat","cats","sand","dogs","and")
     print s
     print wordDict
     print word_break(s, wordDict)
