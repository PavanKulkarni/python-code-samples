
def palindromePairs(words):
    d, res = dict([(w[::-1], i) for i, w in enumerate(words)]), []
    for i, w in enumerate(words):
        for j in xrange(len(w)+1):
            prefix, postfix = w[:j], w[j:]
            if prefix in d and i != d[prefix] and postfix == postfix[::-1]:
                res.append([i, d[prefix]])
            if j>0 and postfix in d and i != d[postfix] and prefix == prefix[::-1]:
                res.append([d[postfix], i])
    return res 	


def print_pp(w_list, words):
    for i in w_list:
        print 'Palindrome Pairs are %s and %s'%(words[i[0]], words[i[1]])

if __name__=='__main__':
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    # abcd and dbca are detected because the prefix is found in the dict but has different index.
    print_pp(palindromePairs(words), words)
