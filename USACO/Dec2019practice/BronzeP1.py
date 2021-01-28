f=open("gymnastics.in", "r")
lines=f.read().split("\n")[1:-1]
f.close()

def intersect(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3

finallist=[]
for i in range(len(lines)):
    # print(lines[i])
    current=[]
    temp=lines[i].split()
    for j in range(len(temp)):
        # print(temp[j+1:])
        for k in temp[j+1:]:
            # print(k)
            # print([temp[j],k])
            current.append([temp[j], k])

    # print(current)
    if i==0:
        finallist=current
    else:
        finallist=intersect(finallist, current)

# print(current)

# print(finallist)
# print(len(finallist))

f=open("gymnastics.out", "w")
f.write(str(len(finallist)))
f.close()
