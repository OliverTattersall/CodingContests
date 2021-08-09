
a=1
b=1

for i in range(2, 10**6+1, 1):
    x= a+b
    # a=b
    # b=x
    a,b = b, x
    if len(str(x))>999:
        print(i+1)
        break

    

