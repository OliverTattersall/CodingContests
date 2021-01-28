times=int(input())
options=[]
for i in range(times):
    options.append(input().split())

print(options)

for i in range(len(options)):
    if len(options[i][2])>=10:
        if int(options[i][2][-10:])>2:
            print(options[i])