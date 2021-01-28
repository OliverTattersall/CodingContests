totalattractions, maxattractions=input().split(" ")
attractions=input().split(" ")
totalattractions=int(totalattractions)
maxattractions=int(maxattractions)
offdays=totalattractions%maxattractions


def go(list1,list2, numperday):
    deleted=[]
    day=[]
    sum1=[]
    sum2=[]
    for i in range(offdays):
        deleted.append(list1[0])
        list1.pop(0)
    #print(list2)
    for i in range(0,len(list1),numperday):
        day=[int(list2[i]),int(list2[i+1]),int(list2[i+2])]
        sum1.append(max(day))
    sum1.append(int(max(deleted)))
    #print(list2)
    #print(offdays)
    for i in range(offdays):
        list2.insert(0, deleted[i])
    deleted=[]
    for i in range(offdays):
        deleted.append(list2[-1])
        list2.pop(-1)
    #print(list2)
    for i in range(0,len(list2), numperday):
        day=[int(list2[i]),int(list2[i+1]),int(list2[i+2])]
        sum2.append(max(day))
    sum2.append(int(max(deleted)))
    if sum(sum1)>=sum(sum2):
        scores.append(sum(sum1))
    elif sum(sum2)>sum(sum1):
        scores.append(sum(sum2))
    


scores=[]
#print(attractions)
if offdays==0:
    sumlist=[]
    for i in range(0,totalattractions,maxattractions):
        day=[int(attractions[i]),int(attractions[i+1]),int(attractions[i+2])]
        sumlist.append(max(day))
    
    scores.append(sum(sumlist))
else:
    go(attractions, attractions, maxattractions)


print(scores[0])