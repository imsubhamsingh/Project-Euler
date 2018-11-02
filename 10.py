import math
import eulib
def primesum():
    ans= sum(eulib.list_prime(1999999))
    return str(ans)
if __name__ == '__main__':
    print(primesum())
