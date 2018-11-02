def compute():
    ans= sum(i for i in range(2,1000000)if i== fifthpower(i))
    return str(ans)
def fifthpower(n):
    return sum(int(c)**5 for c in str(n))

if __name__ == '__main__':
    print(compute())
