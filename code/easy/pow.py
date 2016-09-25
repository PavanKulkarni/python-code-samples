def pow(x,n):
    res = 1
    while n > 0:
       if n%2:
         res = res*x
    
       x = x*x
       n = n/2        
    return x

if __name__=='__main__':
   print pow(5,3)
