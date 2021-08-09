lines, home, goal, escalators = input().split(" ")
lines=int(lines)
home=int(home)
goal=int(goal)
escalators=int(escalators)

paths=[]

options=[]

for i in range(escalators):
    a,b=input().split(" ")
    a=int(a)
    b=int(b)
    paths.append([a,b])
    
def searcher(end, count):
    #print(end)
    if count>escalators:
        return
    if end==home:
        options.append(count)
        # print(options)
        # print("\n"+str(count)+" \n")
    else:
        for i in range(escalators):
            if paths[i][1]==end:
                searcher(paths[i][0], count+1)


searcher(goal, 0)
print(options)
options.sort()

print(options[0])