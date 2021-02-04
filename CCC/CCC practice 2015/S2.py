j = int(input())

a = int(input())

jerseys=[]

sizes ={"S":1, "M":2, "L":3}

for i in range(j):
    jerseys.append(input())

alth = []


for i in range(a):
    alth.append(input().split())

alth.sort(key = lambda x: int(x[1]))
# print(alth)

sum = 0
used = {}
for i in range(a):
    temp = alth[i]
    if temp[1] in used:
        if used[temp[1]]==True:
            continue
    jer = jerseys[int(temp[1])-1]
    if sizes[jer]>=sizes[temp[0]]:
        # print(jer, temp)
        if temp[1] not in used:
            used[temp[1]]=True
            sum+=1
        elif used[temp[1]]==False:
            sum+=1
            used[temp[1]]=True

print(sum)
