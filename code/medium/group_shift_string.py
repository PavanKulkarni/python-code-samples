def gss(s):
    primes = [2,3,5,7,11,13,17,19,23,29,31,37]
    global_m_dict = {}
    for idx,tmp_s in enumerate(s):
        if idx not in global_m_dict:
            global_m_dict[idx] = 1
        for i,x in enumerate(tmp_s):
            global_m_dict[idx] = global_m_dict[idx]*primes[i]
    solution = []
    reverse_index = {}
    for key,val in global_m_dict.iteritems():
       if val not in reverse_index:
            reverse_index[val] = []
       reverse_index[val].append(key)
    for x,y in reverse_index.iteritems():
    	tmp_sol = []
    	for val in y:
    	    tmp_sol.append(s[val])
    	solution.append(tmp_sol)
    return solution



if __name__=='__main__':
    ret = gss(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
    print ret
