n = input()
count=0
for i in range(len(n)-1):
    if n[i]=="2":
        if n[i+1]!="5":
            count+=1


if n[-1]=="2":
    count+=1
print(count)
