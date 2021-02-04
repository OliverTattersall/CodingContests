g = int(input())

p = int(input())

planes = []
spots = {i:True for i in range(1, g+1)}
sum=0

for i in range(p):
    planes.append(int(input()))





for i in range(p):
    landed = False
    for j in range(planes[i], 0, -1):
        if spots[j]==True:
            spots[j]=False
            sum+=1
            landed = True
            break

    if landed ==False:
        break

print(sum)