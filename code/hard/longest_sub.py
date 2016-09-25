def ls(word):
   r_dict = {}
   for idx,i in enumerate(word):
      r_dict[i] = idx
   max_len = 1
   o_dict = set(r_dict.values())
   for i in range(len(word)-1):
       if i in o_dict and i + 1 in o_dict:
           max_len +=1
       else:
           max_len = 1
   return max_len


if __name__=='__main__':
    test = ['abcabcdabcdef', 'abcadefgh', 'abcacdefg']
    for i in test:
        print ls(i)
