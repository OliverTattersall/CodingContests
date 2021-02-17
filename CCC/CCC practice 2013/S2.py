from collections import deque

w = int(input())
n = int(input())
cars = []
for i in range(n):
    cars.append(int(input()))




q = deque()


count=0


for i in range(n):
    # cars.append(int(input()))
    
    q.append(cars[i])
    # print(q)

    if len(q)==5:
        q.popleft()

    if sum(q) <= w:
        count+=1 
    else:
        break

print(count)
