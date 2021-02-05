
n = int(input())

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

if n-1<3:
    print(0)

else:
    top = factorial(n-1)
    bottom = factorial(n-1-3)*factorial(3)
    print(int(top/bottom))
