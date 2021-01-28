N=int(input())
flowers=input().split(" ")

for i in range(len(flowers)):
    flowers[i]=int(flowers[i])



total=len(flowers)





pairs=[]

for i in range(len(flowers)):
    for j in range(i+1, len(flowers)):
        pairs.append([i, j])


for i in range(len(pairs)):
    item=flowers[pairs[i][0]:pairs[i][1]+1]
    average=sum(item)/len(item)
    # print(average, i, j)
    for j in range(pairs[i][0], pairs[i][1]+1, 1):
        if average==flowers[j]:
            total+=1
            break
 
print(total)


