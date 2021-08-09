paths=int(input())
overall=[]
for i in range(paths):
    temp=input().split(" ")
    overall.append(temp)

# print(overall)
time=1000000000
alltime=[]

for i in range(paths):
    temptime=0
    for j in range(1, (int(overall[i][0])+1)):
        temptime+=int(overall[i][j])
    # print(temptime)
    alltime.append(temptime)
    if temptime<time:
        time=temptime

print(alltime)
print(time)