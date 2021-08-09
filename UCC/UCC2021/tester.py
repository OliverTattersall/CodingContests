from functools import lru_cache

@lru_cache(maxsize=100)
def fib(n):
    if n<=2:
        return 1

    return fib(n-1)+fib(n-2)


# x=[]
# # for i in range(80):
# #     x.append(fib(i)%2021+i%50)

# # print(x)
# z={}

# for i in range(200):
#     q=fib(i)%2021
#     z[q]=z.get(q, 0) +1
# # for i in range(39):
# #     z.append(x[i+1]-x[i])

# print(z)





# print(lst)

print(8348234%12931)
