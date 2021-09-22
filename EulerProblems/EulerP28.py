from collections import deque

sum = 0
#sum 3*3 = 1+(1+2)+(1+2*2)+1+6+1+8
# for i in range()
#length of half diaganol -> 1 1*1, 2 3*3, 3 5*5, 4 7*7, 5 9*9


q =deque([1])
count = 0
up = 2
for i in range(2001):
    item = q.popleft()
    if count==4:
        count=0
        up=up+2
    count+=1
    sum+=item
    q.append(item+up)
    
print(sum)