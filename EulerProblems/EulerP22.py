f = open("P22.txt", "r")

names= f.read().replace('"', '').split(",")
names.sort()

sum=0
for i in range(len(names)):

    temp=0
    for j in range(len(names[i])):
        temp+=ord(names[i][j])-64

    temp*=(i+1)
    sum+=temp
print(sum)

