n = int(input())

x = set()


def recur(n, vals):
    if n==0:

        x.add(vals)
        return 

    if n<0:
        return 

    vals4 = (vals[0]+1, vals[1])
    vals5 = (vals[0], vals[1]+1)

    recur(n-4, vals4)
    recur(n-5, vals5)
    # if n>=4:
    #     return recur(n-4)+1

    # if n>=5:
    #     return recur(n-5)+1

    # if n<4:
    #     return 0


# recur(n, (0,0))
# print(recur(n, ()))
# print(len(x))



## second attempt
sum = 0
div = n//20
mod = n%20

if mod==0:
    sum+=1
else:
    recur(mod, (0,0))
    sum+=len(x)

sum+=div
print(sum)

lst = []
for i in range(20):
    x=set()
    recur(i, (0,0))
    lst.append(len(x))
print(lst)
print([0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,0])