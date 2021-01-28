n, k = input().split()

n=int(n)
k=int(k)
cows=[]
cowvisited={}
cowlocs={}
swaps=[]
for i in range(k):
    temp = input().split()
    swaps.append([int(temp[0]), int(temp[1])])


# cows=[i for i in range(n)]
# cowvisited={i:1 for i in range(n)}
# cowlocs = {i:{j:False for j in range(n) for i in range(n)}

for i in range(n):
    cows.append(i)
    cowvisited[i]=1
    temp={}
    for j in range(n):
        temp[j]=False
    cowlocs[i]=temp
    cowlocs[i][i]=True

# print(cows, cowvisited, cowlocs)

    
temp=cows.copy()
test=True
while temp!= cows or test==True:
    test=False
    # print(temp)
    for i in range(k):
        # print(swaps[i][0]-1, swaps[i][1]-1, cowlocs)
        temp[swaps[i][0]-1], temp[swaps[i][1]-1] = temp[swaps[i][1]-1], temp[swaps[i][0]-1]
        if cowlocs[temp[swaps[i][1]-1]][swaps[i][1]-1]==False:
            cowvisited[temp[swaps[i][1]-1]]+=1
            cowlocs[temp[swaps[i][1]-1]][swaps[i][1]-1]=True
        if cowlocs[temp[swaps[i][0]-1]][swaps[i][0]-1]==False:
            cowvisited[temp[swaps[i][0]-1]]+=1
            cowlocs[temp[swaps[i][0]-1]][swaps[i][0]-1]=True

    print(temp)

# print(cowvisited)

for i in range(len(cows)):
    print(cowvisited[i])