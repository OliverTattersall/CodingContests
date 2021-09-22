import random
from collections import deque

# maze = [[1 for i in range(10)]for _ in range(10)]
maze= [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], 
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], 
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], 
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], 
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], 
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]
visited = [[False for _ in range(10)] for _ in range(10)]

# print(maze)
# for i in range(25):
#     x=random.randint(0,9)
#     y=random.randint(0,9)
#     maze[x][y]=0



maze[9][9]=1
maze[0][0]=1

for i in range(10):
    print(maze[i])

q = deque()

src = (0,0)
dest=(9,9)

visited[0][0]=True
q.append((0,0,0))
count=0
while len(q)!=0:

    item = q.popleft()
    if (item[0], item[1])==dest:
        count=item[2]
        break
    if item[0]-1>=0:
        if maze[item[0]-1][item[1]]==1:
            if visited[item[0]-1][item[1]]==False:

                q.append((item[0]-1, item[1], item[2]+1))
                visited[item[0]-1][item[1]]=True

    if item[0]+1<=9:
        if maze[item[0]+1][item[1]]==1:
            if visited[item[0]+1][item[1]]==False:

                q.append((item[0]+1, item[1], item[2]+1))
                visited[item[0]+1][item[1]]=True

    if item[1]-1>=0:
        if maze[item[0]][item[1]-1]==1:
            if visited[item[0]][item[1]-1]==False:
                q.append((item[0], item[1]-1, item[2]+1))
                visited[item[0]][item[1]-1]=True

    if item[1]+1<=9:
        if maze[item[0]][item[1]+1]==1:
            if visited[item[0]][item[1]+1]==False:
                q.append((item[0], item[1]+1, item[2]+1))
                visited[item[0]][item[1]+1]=True

if count!=0:
    print(count)
else:
    print(False)