from collections import deque

nums = input().split()
walks = {}
for i in range(int(nums[1])):
    temp=input().split()
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    if temp[0] in walks:
        walks[temp[0]] = walks[temp[0]]+(temp[1], )
    else:
        walks[temp[0]] = (temp[1], )


switches = []
current = input().split()
# for i in range(int(nums[2])):
#     temp=input().split()
#     temp[0] = int(temp[0])
#     temp[1] = int(temp[1])
#     switches.append(temp)

for i in range(len(current)):
    current[i] = int(current[i])

# print(walks)

for i in range(int(nums[2])):
    temp=input().split()
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    switches.append(temp)


    visited = set([])
    change = current.copy()
    x = change[switches[i][0]-1]
    y = change[switches[i][1]-1]
    change[switches[i][0]-1]=y
    change[switches[i][1]-1] = x
    current = change.copy()
    q = deque([[1,0]])
    # print(current)
    while len(q)!=0:
        temp1 = q.popleft()
        temp = temp1[0]
        time = temp1[1]
        if temp==len(current):
            if time>len(current)-1:
                print(len(current)-1)
            else:
                print(time)
            break
        # i = current.index(temp)

        
        
        if time+1<len(current):
            if temp==current[time]:
                if current[time+1] not in visited:
                    q.append([current[time+1], time+1])

        if temp not in visited:
            visited.add(temp)
            if temp in walks:
                for j in range(len(walks[temp])):
                    if walks[temp][j] not in visited:
                        q.append([walks[temp][j], time+1])

        
        q.append([temp, time+1])

        

        # print(q)
    # print(visited)
