
def seriessum(n):
    ans= sum(i**i for i in range(1,1001))
    return str(ans)[-10:]

print(seriessum(1000))
