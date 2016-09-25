def perm(word):
    if not word:
       # Returning list is important  
       return [word]
    else:
        temp = []
        for k in range(len(word)):
            part = word[:k] + word[k+1:]
            for m in perm(part):
                temp.append(word[k:k+1] + m)
    return temp




if __name__=='__main__':
   print perm('cat')
