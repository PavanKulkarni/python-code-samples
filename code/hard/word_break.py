def word_break(s, wordDict):
        if not s and not wordDict:
            return True
        if not wordDict:
            return False
        if len(s) == 1 and s not in wordDict:
            return False
        DP = [False]*(len(s)+1)
        DP[0] = True
        for i in range(1,len(s)+1):
            for k in range(i+1):
                if DP[k] and s[k:i] in wordDict:
                    DP[i] = True
        return DP[len(s)]	




if __name__=='__main__':
     s = "goalspecial"
     wordDict = ["go","goal","goals","special"]
     print s
     print wordDict
     print word_break(s, wordDict)
