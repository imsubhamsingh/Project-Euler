import logging
import math
logging.basicConfig(level=logging.DEBUG)

#getting factors of anumber
def getfactors(num):
		factors=[]
		for potentialfactor in range(1,int(math.sqrt(num))+1):
			if num % potentialfactor==0:
				factors.append(potentialfactor)
				factors.append(num// potentialfactor)
		return factors
#print(getfactors(121))
logging.debug(getfactors(24))
logging.debug(getfactors(17))
# check for prime
def isprime(num):
	return len(getfactors(num))==2
logging.debug('isprime(24)= %s'%(isprime(24)))
logging.debug('isprime(17)= %s'%(isprime(17)))
logging.debug('isprime(600851475143)= %s'%(isprime(600851475143)))
#finding largest prime factor
allfactors= getfactors(600851475143)
largestfactor=0
for factor in allfactors:
	if isprime(factor) and factor> largestfactor:
		largestfactor=factor
print(largestfactor)
