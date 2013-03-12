import sys
n=int(sys.argv[1])
fib=[0,1]
#for z in range(n):
  #fib.append(fib[z]+fib[z+1])
#print fib[n]

z=0

def fiba(z):
  if z <= n-1:
    z=z+1
    fib.append(fib[z]+fib[z-1])
    fiba(z)
fiba(z)
print fib

