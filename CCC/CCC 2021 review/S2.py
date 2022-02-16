r = int(input())
c = int(input())
k = int(input())

rows = [0 for _ in range(r)]
cols = [0 for _ in range(c)]

changes = []
for i in range(k):
    type, place = input().split(" ")
    place = int(place)-1
    if type == "R":
        rows[place]+=1
    else:
        cols[place]+=1

for i in range(r):
    rows[i] = rows[i]%2+1
    
for i in range(c):
    cols[i] = cols[i]%2+1

# print(rows, cols)

sum = 0

for i in range(r):
    for j in range(c):
        if rows[i]*cols[j]==2:
            sum+=1

print(sum)
