def base10ToBase2(n):

    return int(bin(n)[2:])


sum = 0

for i in range(0, 1000000, 1):
    temp = str(i)[::-1]
    if temp==str(i):
        x = base10ToBase2(i)
        if str(x) == str(x)[::-1]:
            sum+=i


print(sum)
