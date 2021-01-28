N=int(input())
cows=[]

soreastcows=[]
eastcows=[]
easteqs=[]


sornorthcows=[]
northcows=[]
northeqs=[]


answers={}

for i in range(N):
    item=input().split(" ")
    cows.append(item)
    if item[0]=="N":
        northcows.append(item)
        # northeqs.append(item[1])


    else:
        eastcows.append(item)
        # easteqs.append(item[2])



# print(cows)
# print(northcows)
# print(eastcows)
# print(easteqs)
# print(northeqs)
sornorthcows=northcows.copy()
soreastcows=eastcows.copy()
sornorthcows.sort(key=lambda x: int(x[1]))
soreastcows.sort(key=lambda x:int(x[2]))




for i in sornorthcows:
    northeqs.append(i[1])
for i in soreastcows:
    easteqs.append(i[2])

def addanswers(n,m, d):
    if d=="N":
        print(n,m)
        diff=int(northcows[n][2])-int(northcows[m][2])
        print(diff)
        if diff>0:
            ind=cows.index(northcows[m])
            answers[ind]=diff
            cows.remove(cows[ind])
        else:
            ind=cows.index(northcows[n])
            answers[ind]=(diff*(-1))
            cows.remove(cows[ind])
    else:
        diff=int(eastcows[n][2])-int(eastcows[m][2])
        if diff>0:
            ind=cows.index(eastcows[m])
            answers[ind]=diff
            cows.remove(cows[ind])
        else:
            ind=cows.index(eastcows[n])
            answers[ind]=(diff*(-1))
            cows.remove(cows[ind])

# num=0
# while num < len(northeqs):

#     if northeqs.count(northeqs[num])>1:
#         first=northeqs.index(northeqs[num])
#         second=northeqs.index(northeqs[num], first+1)
#         addanswers(first, second, "N")
#         northeqs.remove(northeqs[second])
        
        
#     num+=1

# num1=0
# while num < len(easteqs):

#     if easteqs.count(easteqs[num1])>1:
#         first=easteqs.index(easteqs[num1])
#         second=northeqs.index(easteqs[num1], first+1)
#         addanswers(first, second, "E")
#         easteqs.remove(easteqs[second])
        
        
#     num1+=1



# print(cows)
# print(soreastcows)
# print(sornorthcows)
# # print(answers)

# print(easteqs)
# print(northeqs)

intersects=[]
for i in range(len(easteqs)):
    for j in range(len(northeqs)):
        if int(northeqs[j])<int(soreastcows[i][1]) or int(easteqs[i])<int(sornorthcows[j][2]):
            pass
        else:
            intersects.append([northeqs[j],easteqs[i]])

# print(intersects)



# for i in range(len(eastcows)):
#     # print(eastcows[i])
#     j=0
#     while j < len(intersects):
#         if soreastcows[i][2]==intersects[j][1]:

#             dist=int(intersects[j][0])-int(soreastcows[i][1])
            
#             # if dist==7:
#             #     print(soreastcows[i], i)
#             #     print(dist, j)
#             #     print(intersects[j])
#             #     print(intersects)
#             for k in range(len(sornorthcows)):
#                 if k==1:
#                     print(j, k, sornorthcows[k], intersects, soreastcows[i])

#                 if sornorthcows[k][1]==intersects[j][0]:
                    
                    
#                     dist2=int(intersects[j][1])-int(sornorthcows[k][2]) 
#                     if k==1:
#                         print(sornorthcows[k], intersects[j], dist, dist2)
#                     # if k==1:
#                         # print(dist, dist2, i, j, k)
#                     # print(dist2)
#                     if dist>dist2:
#                         if k==1:
#                             print(soreastcows[i], intersects)
#                         ind=cows.index(soreastcows[i])
#                         answers[ind]=dist
#                         num2=0

#                         # print(sornorthcows[k], intersects[j], k, i)

#                         while num2<len(intersects):
#                             if intersects[num2][1]==soreastcows[i][2]:
#                                 # if intersects[num2]==['11', '5']:
#                                 #     print(i, j, k, num2)
#                                 intersects.remove(intersects[num2])
#                                 # print("hello")
#                             num2+=1
#                     elif dist==dist2:
#                         # print(k)
#                         pass
#                     elif dist<dist2:
#                         ind=cows.index(sornorthcows[k])
#                         answers[ind]=dist2
#                         num2=0
#                         # print(sornorthcows[k])
#                         while num2<len(intersects):
#                             if intersects[num2][0]==sornorthcows[k][1]:
#                                 # if intersects[num2]==['11', '5']:
#                                     # print(i, j, k, num2)
#                                 intersects.remove(intersects[num2])
#                             num2+=1
#                     break
#         j+=1
#     # print(intersects)
    
# print(cows)
# print(answers)
# print(intersects)

for i in range(len(sornorthcows)):

    j=0
    while j < len(intersects):

        if sornorthcows[i][1]==intersects[j][0]:
            dist=int(intersects[j][1])-int(sornorthcows[i][2])

            for k in range(len(soreastcows)):
                
                m=0
                while m < len(intersects):

                    if soreastcows[k][2]==intersects[m][1]:

                        dist2=int(intersects[m][0])-int(soreastcows[k][1])

                        if dist > dist2:

                            ind=cows.index(sornorthcows[i])
                            answers[ind]=dist

                            num=0

                            while num < len(intersects):

                                if intersects[num][0]==sornorthcows[i][1]:

                                    intersects.remove(intersects[num])

                                num +=1

                        elif dist==dist2:
                            pass
                        
                        elif dist<dist2:

                            ind=cows.index(soreastcows[k])
                            answers[ind]=dist2

                            num = 0

                            while num < len(intersects):

                                if intersects[num][1]==soreastcows[k][2]:

                                    intersects.remove(intersects[num])

                                num+=1
                        
                        break

                    m+=1

        j+=1

                    

print(answers)


for i in range(len(cows)):
    print(answers.get(i, "Infinity"))
    
# print("5")