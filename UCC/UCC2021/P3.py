n=int(input())
slices=[0 for i in range(n)]

sec = input().split()
sec[0]=int(sec[0])-1
sec[1]=int(sec[1])-1
rang = sec[1]-sec[0]+1

r = int(input())
count=0
# runs = []
for i in range(r):
    temp=input().split()
    temp[0]=int(temp[0])-1
    temp[1]=int(temp[1])-1
    # runs.append(temp)
    # for j in range(temp[0], temp[1]+1,1):
    #     slices[j]+=1

    if temp[1]>=sec[1] and temp[0]<=sec[0]:
        count+=rang

    elif temp[1]<sec[0] or temp[0]>sec[1]:
        pass
    else:
        difr=0
        difl=0
        if temp[1]<sec[1]:
            difr=sec[1]-temp[1]
        if temp[0]>sec[0]:
            difl=temp[0]-sec[0]
        count+=rang-difl-difr
    

    


# sum=0
# for i in range(sec[0], sec[1]+1,1):
#     sum+=slices[i]

print(count)