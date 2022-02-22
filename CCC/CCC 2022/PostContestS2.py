x = int(input())
together = []
tog = {}
for i in range(x):
    temp= input().split(" ")
    together.append(temp)
    tog[temp[0]] = tog.get(temp[0], set())
    tog[temp[0]].add(temp[1])
    tog[temp[1]] = tog.get(temp[1], set())
    tog[temp[1]].add(temp[0])

# print(tog)
apart=[]
apar = {}
y = int(input())
for j in range(y):
    temp = input().split(" ")

    apar[temp[0]] = apar.get(temp[0], set())
    apar[temp[0]].add(temp[1])
    apar[temp[1]] = apar.get(temp[1], set())
    apar[temp[1]].add(temp[0])


g = int(input())

groups = []
gsets = []
for _ in range(g):
    temp = input().split(" ")
    groups.append(temp)
    gsets.append(set(temp))

# print(gsets)
# print(apar, tog)
cond = set()
count = 0
for i in range(g):
    for k in range(len(groups[i])):
        
        if groups[i][k] in tog:
            for name in tog[groups[i][k]]:
                if name not in gsets[i]:
                    temp = (groups[i][k], name, "t")
                    temp2 = (name, groups[i][k], "t")
                    if temp not in cond and temp2 not in cond:
                        cond.add(temp)
                        cond.add(temp2)
                        count+=1
        
        if groups[i][k] in apar:
            for name in apar[groups[i][k]]:
                if name not in gsets[i]:
                    temp = (groups[i][k], name, "t")
                    temp2 = (name, groups[i][k], "t")
                    if temp not in cond and temp2 not in cond:
                        cond.add(temp)
                        cond.add(temp2)
                        count+=1


# if y!=0:
#     print(3)
# else:
#     print(count)
print(count)