def fact(n):
    if n==1:
        return 1

    return fact(n-1)*n

x = [z for z in str(fact(100))]
x = list(map(int, x))
print(sum(x))