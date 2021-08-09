n, x = input().split()
n=int(n)
x=int(x)

coins=[]
for i in range(n):
    temp=input().split()
    temp[0]=int(temp[0])
    temp[1]=int(temp[1])

    coins.append(temp)
max=0

for i in range(n):
    if coins[i][0]<=x:
        temp = coins[i][0]*coins[i][1]
        if temp>max:
            max=temp
    else:
        temp=x*coins[i][1]
        if temp>max:
            max=temp
print(max)