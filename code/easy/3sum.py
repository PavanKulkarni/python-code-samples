import random

def three_sum(a, target):
   a.sort()
   n = len(a)
   res = set()
   if n < 3:
       return []

       
   for i in range(n-2):
       # If duplicate items not allowed , if allowed then remove (a[i] != a[i-1]) check
       if a == 0 or a[i] != a[i-1]:
            j = i + 1
            k = n -1
            while j < k:
                sum = a[i] + a[j] + a[k]
                if sum == target:
                   res.add((a[i], a[j], a[k]))
                   j += 1
                   k -= 1
                elif sum < target:
                   j += 1
                else:
                   k -= 1
   return list(res)

if __name__=='__main__':
  a = [random.randint(0, 10) for i in range(10)]
  print a
  print three_sum(a, 9)


