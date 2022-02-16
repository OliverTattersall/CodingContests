# incorrect


# lst = [[6,8,3],[1,4,1], [14,5,2]]
def time1(lst, x):
    if abs(x-lst[0])<=lst[2]:
        return 0
    else: 
        return (abs(x-lst[0])-lst[2])*lst[1]


def time(lst, x):
    fun = lambda y:time1(y,x)
    # print(fun([10,4,3]))
    return sum(map(fun, lst))



def mintwo(lst, d, i, j):
    if j-i<3000:
        # print("hello", i, j)
        minz = float("inf")
        for l in range(i, j+1, 1):
            # print(l)
            temp = time(lst, l)
            # print(temp)
            if temp<minz:
                minz =temp
        return [minz]

    min1 = float("inf")
    min2 = float("inf")
    while i<j:
        temp = time(lst, i)
        if temp<min1:
            min2 = min1
            min1 = temp
        elif temp <min2:
            min2 = temp
        i=i+d
    return [i,j]

# print(time(lst, 9))
# y = lambda l:sum(map(lambda x:x+1, l))
# print(y([1,2]))

n = int(input())
people = []
minLoc = float("inf")
maxLoc = float("-inf")
currentmin = time(people, minLoc)

for i in range(n):
    temp = list(map(int, input().split(" ")))
    if temp[0]>maxLoc:
        maxLoc = temp[0]
    if temp[0]<minLoc:
        minLoc=temp[0]
    people.append(temp)

# print(people, minLoc, maxLoc)
i = minLoc
j = maxLoc
end = 0
# while True:
#     if(j-i)<=0:
#         end = j
#         break
#     temptime1 = time(people,i)
#     temptime2 = time(people, j)

#     if temptime1<temptime2:
#         j=j - (j-i)//2
#     else:
#         i=i+(j-i)//2

d = (j-i)//5
while True:
    res = mintwo(people, d, i,j)
    if len(res)==1:
        end = res[0]
        break
    else:
        i = res[0]
        j = res[1]
        d = (j-i)//5

# end = time(people, end)
print(end)