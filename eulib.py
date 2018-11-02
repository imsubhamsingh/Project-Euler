# Given integer x, this returns the integer floor(sqrt(x)).
import math
def sqrt(n):
    root= n/2
    for k in range(20):
        root= (1/2)* ((root+n)/root)
    return root
# Tests whether x is a perfect square, for any integer x.
def is_square(n):
    if n<0:
        return False
    y=sqrt(n)
    return y*y==x
#test to check prime niumber
def is_prime(n):
    if n<=2:
        return False
    elif n<=3:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3,int(sqrt(n))+1,2):
            if n%i ==0:
                return False
        return True
## Sieve of Eratosthenes
def  list_primality(n):
    result = [True]*(n+1)
    result[0]=result[1]=False
    for i in range(int(sqrt(n))+1):
        if result[i]:
            for j in range(i*i,len(result),i):
                    result[j]= False
    return result
def list_prime(n):
    return [i for (i,is_prime) in enumerate(list_primality(n)) if is_prime]

class memoize(object):

	def __init__(self, func):
		self.func = func
		self.cache = {}

	def __call__(self, *args):
		if args in self.cache:
			return self.cache[args]
		else:
			val = self.func(*args)
			self.cache[args] = val
			return val

#bionomial coeficiant
def bionomial(n,r):
    assert 0<=r<=n
    return math.factorial(n)//(math.factorial(r)* math.factorial(n-r))
