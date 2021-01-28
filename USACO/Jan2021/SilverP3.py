n=int(input())
grid=[]
places=[]
all=[]
for i in range(n):
    temp=input().split()
    temp2=[]
    for j in range(n):
        temp[j]=int(temp[j])
        temp2.append(".")
        all.append(temp[j])

    grid.append(temp)
    places.append(temp2)

# print(grid, places)
# temp=[]
# sum=0
# for i in range(n-1):
#     for j in range(n-1):
#         temp=[grid[i][j], grid[i][j+1], grid[i+1][j], grid[i+1][j+1]]
#         x = (float("-inf"), None)
#         for k in range(4):
#             if temp[k]>x[0]:
#                 x=(temp[k], k)

#         if x[1] ==0:
#             places[i][j]="C"
#         elif x[1]==1:
#             places[i][j+1]="C"
#         elif x[1]==2:
#             places[i+1][j]="C"
#         elif x[1]==3:
#             places[i+1][j+1]="C"

# # print(places)
            
# for i in range(4):
#     print(places[i])



    
if n%2==0:
    sum=0
    for i in range(n**2//2):
        max=(float("-inf"), None)
        for j in range(n*n):
            if all[j]>max[0]:
                max=(all[j], j)
        sum+=max[0]
        all[max[1]]=float("-inf")
    print(sum)

else:
    sum1=0
    for i in range(n**2//2+n//2+1):
        max=(float("-inf"), None)
        for j in range(n*n):
            if all[j]>max[0]:
                max=(all[j], j)
        sum1+=max[0]
        all[max[1]]=float("-inf")    

    sum2=0
    for i in range(n**2//2+1):
        max=(float("-inf"), None)
        for j in range(n*n):
            if all[j]>max[0]:
                max=(all[j], j)
        sum2+=max[0]
        all[max[1]]=float("-inf")  

    print(max(sum1, sum2))