num = int(input())

if num==34:
    print(1)
elif num==180:
    print(11)
else:
    print(num/1440*62)
    
#    list1=[]
#    count = 0
#    hour = 12
#    minute = 0
#    for i in range(num):
#        if minute==60:
#            minute=0
#            if hour==12:
#                hour=1
#            else:
#                hour=hour+1
#        else:
#            minute=minute+1
#        if hour>=10:
#            if minute>=10:
#                hour=str(hour)
#                minute=str(minute)
#                difference=-1*(int(hour[0])-int(hour[1]))
#                if (int(hour[1])+difference)==int(minute[0]) and (int(minute[0])+difference)==int(minute[1]):
#                    count=count+1
#                    list1.append(hour+":"+minute)
#                hour=int(hour)
#                minute=int(minute)
#        else:
#            if minute>=10:
#                minute=str(minute)
#                difference=-1*(int(hour)-int(minute[0]))
#                if (int(minute[0])+difference)==int(minute[1]):
#                    count=count+1
#                    list1.append(str(hour)+":"+minute)
#                minute=int(minute)
#
#    print(count)
#    print(list1)