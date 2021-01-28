number=int(input())
times=int(input())+1
shiftysum = 0

for i in range(times):
    shiftysum=shiftysum +(number*(10**i))

print(shiftysum)