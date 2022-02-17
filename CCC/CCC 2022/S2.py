x = int(input())

tog = {}
for i in range(x):
    temp= input().split(" ")

    tog[temp[0]] = temp[1]
    tog[temp[1]] = temp[0]

print(tog)
# apart=[]
apar = {}
y = int(input())
for j in range(y):
    temp = input().split(" ")

    apar[temp[0]] = temp[1]
    apar[temp[1]] = temp[0]

g = int(input())

groups = []
gsets = []
for _ in range(g):
    temp = input().split(" ")
    groups.append(temp)
    gsets.append(set(temp))

print(gsets)
cond = set()
count = 0
for i in range(g):
    for k in range(len(groups[i])):

        # checks if any togethers get violated
        if groups[i][k] in tog:
            print(gsets[i])
            if tog[groups[i][k]] not in gsets[i]:

                temp = (groups[i][k], tog[groups[i][k]], "t")
                temp2 = (tog[groups[i][k]], groups[i][k], "t")
                if temp not in cond and temp2 not in cond:
                    cond.add(temp)
                    cond.add(temp2)
                    count+=1

        # checks if any aparts are together, violated
        if groups[i][k] in apar:
            if apar[groups[i][k]] in gsets[i]:
                temp = (groups[i][k], apar[groups[i][k]], "a")
                temp2 = (apar[groups[i][k]], groups[i][k], "a")
                if temp not in cond and temp2 not in cond:
                    cond.add(temp)
                    cond.add(temp2)
                    count+=1


print(count)