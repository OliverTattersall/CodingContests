#not done
#patterns are getting repeated try using tuples to solve

coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins.reverse()

# tus = set()
# def solve(n, dct, tu):
#     if n==0:
#         # print(tu)
#         tus.add(tu)
#         return 1
       
#     # if n not in dct:


#     sum=0 
#     for i in range(len(coins)):
#         if n-coins[i]>=0:
#             sum=sum+solve(n-coins[i], dct, tu+(coins[i], ))
            
#         # dct[n]=sum

#     # return dct[n]
#     return sum

# solved={}
# print(solve(200, solved, ()))
# print(tus)

tus = set()
visited = set()
count = [0]
def solve(n, tu):
    tu = tuple(sorted(tu))
    if tu not in visited:
        visited.add(tu)
        if n==0:
            if tu not in tus:
                tus.add(tuple(sorted(tu)))
                count[0]+=1
            
        for i in range(len(coins)):
            if n-coins[i]>=0:
                solve(n-coins[i], tu+(coins[i], ))

solve(200, ())
print(count)
# print(tus)