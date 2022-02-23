import math
f = open("P42.txt", "r")

x = f.read().split('","')
x[0] = x[0][1:]
x[-1] = x[-1][:-1]

t = lambda x: int(0.5*x*(x+1))

spec = set()

for i in range(1, 40, 1):
    spec.add(t(i))
count = 0


for i in x:
    sum = 0
    for j in range(len(i)):
        sum+=ord(i[j])-64
    if sum in spec:
        count+=1
print(count)
def quadratic(c, pos):
    if 1-4*c>0:
        if pos:

            val = (-1+math.sqrt(1-4*c))/2

            return val
        else:
            return 0.5
    else:
        return 0.5

count=0
for i in x:
    sum = 0
    for j in range(len(i)):
        sum+=ord(i[j])-64

    p = quadratic(- 2*(sum), True)
    if int(p)==p:
        count+=1
print(count)

