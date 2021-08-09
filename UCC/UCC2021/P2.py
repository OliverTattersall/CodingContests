n=int(input())
nums=input().split()
for i in range(n):
    nums[i]=int(nums[i])

max=0
temp=0
for i in range(n):
    if nums[i]%2==1:
        if temp>max:
            max=temp
        
        temp=0
    else:
        temp+=nums[i]

if temp>max:
    max=temp
print(max)