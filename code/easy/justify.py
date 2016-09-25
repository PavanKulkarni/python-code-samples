import math
def fullJustify(words, maxWidth):
        spaces = 0
        local_counter = 0
        width_tuple_list = []
        for idx, i in enumerate(words):
            if (local_counter + len(i)) > maxWidth:
                spaces = maxWidth - local_counter
                local_counter = 0
                width_tuple_list.append((idx-1, spaces+1))
                spaces = 0
            local_counter += (len(i) + 1)
        width_tuple_list.append((idx, 0)) 
        prev_idx = 0
        is_even = False
        for p_tup in width_tuple_list:
             if p_tup[0] % 2:
                 is_even = True
             divisor = p_tup[0] - prev_idx
             if divisor == 0:
                 divisor = 1
             t_spaces = int(math.floor((p_tup[1]) / divisor))
             if not t_spaces:
                 t_spaces = 1
             tmp = []
             for idx,t in enumerate(words[prev_idx:p_tup[0]+1]):
                  if idx == (p_tup[0] - prev_idx) and not is_even:
                       t_spaces += 1
                  tmp.append('%s%s' % (t, t_spaces*' '))
             # print tmp
             print ''.join(tmp)
             prev_idx=p_tup[0]+1
        return width_tuple_list  

if __name__=='__main__':
	a = ["This", "is", "an", "example", "of", "text", "justification."]
	print fullJustify(a, 16)
	
