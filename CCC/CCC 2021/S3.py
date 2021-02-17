n = int(input())

friends = []

for i in range(n):
    temp=input().split()
    for j in range(3):
        temp[j] = int(temp[j])

    friends.append(temp)

def solve(n, friends):
    if n==1:
        return 0
    friends.sort(key = lambda x:x[0])
    start = friends[0][0]
    end = friends[-1][0]
    min = float("inf")
    for i in range(start+1, end, 1):
        sum = 0
        for j in range(n):
            temp = abs(friends[j][0]-i)
            if temp<=friends[j][2]:
                sum+=0
            else:
                sum+=friends[j][1]*(temp-friends[j][2])
        if sum<min:
            min=sum
        

    return min

print(solve(n, friends))
