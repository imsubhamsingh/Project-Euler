import math
def compute(n):
    for i in range(n):
        n=n%100
        n=n//10
        print(n)

if __name__ == '__main__':
    print(compute(145))
