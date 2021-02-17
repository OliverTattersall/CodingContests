n, m = input().split()
n = int(n)
m = int(m)

rules = []
for i in range(m):
    temp = input().split()
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    rules.append(temp)

nums = [0 for i in range(n)]

for i in range(m):
    if rules[i][0]==rules[i][1]:
        nums[i] = rules[i][2]

    
