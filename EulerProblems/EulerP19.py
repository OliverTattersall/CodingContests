months={0: 31, 1: 28, 2: 31, 3: 30, 4: 31, 5: 30, 6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31}
day=0
leap=1
count=0

for y in range(1901, 2001):
    for m in range(12):
        x=months[m]
        if m==1 and leap==4:
            x+=1
            leap=-1
        for d in range(x):
            if day==6 and d==0:
                count+=1

            if day==6:
                day=0
            else:
                day+=1
    
    leap+=1

            
print(count)


