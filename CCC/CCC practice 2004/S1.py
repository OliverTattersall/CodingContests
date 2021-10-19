n = int(input())

sets=[]
for _ in range(n):
    temp = [input(), input(), input()]
    sets.append(temp)


result = [True for _ in range(n)]
for i in range(n):

    for j in range(3):
        for k in range(3):
            if j!=k and len(sets[i][j])<=len(sets[i][k]):
                if sets[i][k][0:len(sets[i][j])]==sets[i][j] or sets[i][k][len(sets[i][k])-len(sets[i][j]):]==sets[i][j]:
                    result[i]=False
                    break

for i in range(n):
    if result[i]:
        print("Yes")
    else:
        print("No")