import eulib
def compute():
    ans= sum(i for i in range(1,90000) if is_pandigital(i))
    return str(ans)

def is_pandigital(n):
    for i in range(1,int(eulib.sqrt(n))+1):
        if n%i==0:
            temp=str(n)+str(i)+str(n//i)
            if "".join(sorted(temp))=='123456789':
                return True
    return False
if __name__ == '__main__':
    print(compute())
