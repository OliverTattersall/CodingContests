from collections import deque

k = int(input())

nums = deque()

for i in range(k):
    temp = int(input())
    if temp==0:
        nums.pop()
    else:
        nums.append(temp)


nums = list(nums)
sum=0
for i in range(len(nums)):
    sum+=nums[i]

print(sum)

