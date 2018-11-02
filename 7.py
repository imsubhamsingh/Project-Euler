import math
def isprime(n):
    if n<2:
        return "NOt a isprime"
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def nthprime(n):
    numberofprime=0
    prime=1
    while numberofprime<n:
        prime+=1
        if isprime(prime):
            numberofprime+=1
    return prime
print(nthprime(10))
