import eulib
def compute():
    ans= sum(1 for n in range(0,101)
             for r in range(0,n+1)
             if eulib.bionomial(n,r)>1000000)
    return str(ans)

if __name__ == '__main__':
    print(compute())
