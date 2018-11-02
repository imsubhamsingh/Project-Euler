def compute():
    ans= sum(int(i) for i in str((factorial(100))))
    return str(ans)
def factorial(n):
    if n<=1:
        return nd
    else:
        return n*factorial(n-1)

if __name__ == '__main__':
    print(compute())
