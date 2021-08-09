nums=set()


def collatz(n):
    count=0
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=n*3+1  
        count+=1
        nums.add(n)
    return count+1


print(collatz(13))

large=0
maxed=0
for i in range(10**6-1, 500000, -1):
    if i not in nums:
        nums.add(i)
        item=collatz(i)
        if item>maxed:
            large=i
            maxed=item

print(large)
