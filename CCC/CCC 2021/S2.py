m = int(input())
n = int(input())

canvas = [[False for _ in range(n)] for _ in range(m)]

k = int(input())
strokes = []
for i in range(k):
    temp = input().split()
    temp[1] = int(temp[1])
    strokes.append(temp)

sum = 0
skip =False
for i in range(k):
    temp = strokes[i]
    if i<k-1:
        if temp ==strokes[i+1]:
            skip=True
            continue
    if skip:
        skip=False
        continue
    print(temp)
    if temp[0]=="R":
        for j in range(n):
            if canvas[temp[1]-1][j]==True:
                canvas[temp[1]-1][j]=False
                sum-=1
            elif canvas[temp[1]-1][j]==False:
                canvas[temp[1]-1][j]=True
                sum+=1
    else:
        for j in range(m):
            if canvas[j][temp[1]-1]==True:
                canvas[j][temp[1]-1]=False
                sum-=1
            elif canvas[j][temp[1]-1]==False:
                canvas[j][temp[1]-1]=True
                sum+=1

# sum=0
# for i in range(m):
#     for j in range(n):
#         if canvas[i][j]==True:
#             sum+=1

print(sum)
            