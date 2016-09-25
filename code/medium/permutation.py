def perm(word):
    print '1: %s' % word
    if not word:
        return [word]
    else:
        temp = []
        for k in range(len(word)):
            part = word[:k] + word[k+1:]
            print '2: %s' % part
            for m in perm(part):
                print '3: %s and %s' % (word[k:k+1], m)
                temp.append(word[k:k+1] + m)
        return temp

if __name__=='__main__':
    print perm('cat')
