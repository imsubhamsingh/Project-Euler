import itertools
def solve():
    digits=1000
    prev=1
    curr=0
    for i in itertools.count():
        if len(str(curr))>digits:
            raise RuntimeError("not found")
        elif len(str(curr))==digits:
            return str(i)
        prev,curr=curr,curr+prev

if __name__ == '__main__':
    print(solve())
