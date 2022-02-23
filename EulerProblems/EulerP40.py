end = ''
for i in range(1,1000000, 1):
    end+=str(i)

prod = 1
for i in range(7):
    prod *= int(end[10**i-1])
print(prod)