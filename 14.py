import sys,eulib
def compute():
	#sys.setrecursionlimit(3000)
	ans = max(range(1, 1000000), key=colentz_algo)
	return str(ans)
#@eulib.memoize
def colentz_algo(x):
    if x == 1:
        return 1
    elif x%2==0:
         y= x//2
    else:
        y= 3*x+1
    return colentz_algo(y)+1
if __name__ == '__main__':
    print(compute())
