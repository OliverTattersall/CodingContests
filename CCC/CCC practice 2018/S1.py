N=int(input())
villages=[]
for i in range(N):
    villages.append(int(input()))

villages.sort()

sizes=[0 for _ in range(N)]

sizes[0]=float("inf")
sizes[-1]=float("inf")


for i in range(1, N-1):
    sizes[i]=villages[i]-((villages[i-1]+villages[i])/2)+((villages[i]+villages[i+1])/2)-villages[i]


print(min(sizes))