# from functools import lru_cache

# @lru_cache(maxsize=10)
# def fib(n):
#     if n<=2:
#         return 1

#     return fib(n-1)+fib(n-2)

n=int(input())

fib=[1,1]
for i in range(2, n):
    fib.append(fib[i-1]+fib[i-2])

# print(fib)
tramps = []
for i in range(n):
    tramps.append(fib[i]%2021+(i+1)%50)

# print(tramps)

walkedb={}
def solve(i):

    if i==n:
        print("hello")
        return 0
    walkr=float("inf")
    if i not in walkedb:
        if i-1!=0:
            # print(i)
            walkedb[i]=True
            walkr = solve(i-1)+1


    if i + tramps[i-1]>n:
        
        jump=float("inf")
    else:
        jump=solve(i+tramps[i-1])+1

    walkf=solve(i+1)+1
       
    # print(min(jump, walkr, walkf))
    if min(jump, walkr, walkf)==4:
        print(i)
    return min(jump, walkr, walkf)

print(solve(1))