n, c, r = input().split()
n=int(n)
c=int(c)
r=int(r)
jars=[c for i in range(n)]
rounds=[]
for i in range(r):
    temp = int(input())
    rounds.append(temp)

# print(jars)

for i in range(r):
    for j in range(rounds[i]-1, n, rounds[i]):
        if jars[j]!=0:
            jars[j]=jars[j]-1

# print(jars)
print(sum(jars))