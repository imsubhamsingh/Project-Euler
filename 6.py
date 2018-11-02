def solve():
    n=100
    s= sum(i for i in range(1,n+1))
    s2= sum(i**2 for i in range(1,n+1))
    result = (s**2-s2)
    return (result)
if __name__ == '__main__':
    print(solve())
