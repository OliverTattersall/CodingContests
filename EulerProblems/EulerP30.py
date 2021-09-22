sums={0: 0, 1: 1, 2: 32, 3: 243, 4: 1024, 5: 3125, 6: 7776, 7: 16807, 8: 32768, 9: 59049}
sum=0
for i in range(10,1000000, 1):
    temp = 0
    for j in range(len(str(i))):
        temp+= sums[int(str(i)[j])]
    if temp==i:
        sum+=i
print(sum)