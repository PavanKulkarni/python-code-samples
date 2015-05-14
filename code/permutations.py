def find_permutations(word):
    if not word:
        return [word]
    else:
        temp = []
        for k in range(len(word)):
            part = word[:k] + word[k+1:]
            for m in find_permutations(part):
                temp.append(word[k:k+1] + m)
        return temp

if __name__=='__main__':
    input_string = 'cat'
    permutations = find_permutations(input_string)
    print permutations