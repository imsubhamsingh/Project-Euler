'''
for a in range(3,1000):
    for b in range(a+1,999):
        csquared= a**2+b**2
        c=csquared**0.5
        if a+b+c==1000:
            product= a*b*c
            print(product)
            print(c)
            break
'''
def compute():
	PERIMETER = 1000
	for a in range(1, PERIMETER + 1):
		for b in range(a + 1, PERIMETER + 1):
			c = PERIMETER - a - b
			if a * a + b * b == c * c:
				# It is now implied that b < c, because we have a > 0
				return str(a * b * c)


if __name__ == "__main__":
	print(compute())
