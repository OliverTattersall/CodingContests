test=int(input())
cost=0
costs=[]
for i in range(test):
    storestuff=[]
    neededstuff=[]
    stores=int(input()) 
    for j in range(stores):
        items=int(input())
        for k in range(items):
            storestuff.append(input().split(" "))
    need=int(input())
    for j in range(need):
        neededstuff.append(input().split(" "))

    for j in range(len(neededstuff)):
        temp=[]
        for k in range(len(storestuff)):
            if storestuff[k][0]==neededstuff[j][0]:
                temp.append([int(storestuff[k][1]), int(storestuff[k][2])])
        
        temp=sorted(temp)
        #print(temp)
        for k in range(len(temp)):
            if int(neededstuff[j][1])>temp[k][1]:
                cost+=(temp[k][0]*temp[k][1])
                neededstuff[j][1]=int(neededstuff[j][1])-temp[k][1]
            else:
                cost+=(temp[k][0]*int(neededstuff[j][1]))

    # print(cost)
    costs.append(cost)

for i in range(len(costs)):
    print(costs[i])