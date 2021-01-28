from collections import deque
import heapq


alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
N=int(input())
roads1=[]
roads={}
towns={}
graph={}

for i in range(N):
    temp=input().split()
    temp[1]=int(temp[1])
    roads1.append(temp)

    roads[temp[0]]=temp[1]
    roads[temp[0][::-1]]=temp[1]

    
    towns[temp[0][0]]=towns.get(temp[0][0], 0)+1
    towns[temp[0][1]]=towns.get(temp[0][1], 0)+1

    if temp[0][0] not in graph:
        graph[temp[0][0]]={}
    if temp[0][1] not in graph:
        graph[temp[0][1]]={}
    graph[temp[0][0]][temp[0][1]]=temp[1]
    graph[temp[0][1]][temp[0][0]]=temp[1]

print(graph)
paths=[]
for i in range(5):
    paths.append(input())


print(roads)
towns=list(towns)
n=len(towns)

###repeated section
for j in range(5):
    start=paths[j][0]
    finish=paths[j][1]
    visited = {}
    costs={}
    for i in range(n):
        costs[towns[i]]=float("inf")
        visited[towns[i]] = False
    # print(costs)

    queue=deque()
    queue.append(start)
    visited[start]=True
    costs[start]=0

    


    while len(queue)!=0:
        item=queue.popleft()
        for i in range(len(alphabet)):
            if item+alphabet[i] in roads:
                if visited[alphabet[i]]==False:
                    queue.append(alphabet[i])

                temp = costs[item] + roads[item+alphabet[i]]
                costs[alphabet[i]]=min(temp, costs[alphabet[i]])

        visited[item]=True
        # if j==1:
            # print(costs)
    print(costs[finish])

    q = []
    