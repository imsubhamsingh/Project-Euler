def solve():
    size=1001
    ans=1
    ans+= sum(4*n*n-6*(n-1) for n in range(3,size+1,2))
    return str(ans)

if __name__ == '__main__':
    print(solve())
