f=open("milkvisits.in","r")
lines=f.read().split("\n")[0:-1]
f.close()

# print(lines)
count=lines[0].split(" ")
cows=lines[1]
paths=[]
friends=[]
for i in range(2, int(count[0])+int(count[1])+1, 1):
    # print(i)
    if i<int(count[0])+1:
        paths.append(lines[i].split(" "))
    else:
        friends.append(lines[i].split(" "))

# print(cows)
# print(paths)
# print(friends)

def travelpath(start, goal, milk, destination=False, getmilk=False, lstOfInd=[]):
    if goal==start:
        return [start, goal, milk, destination, getmilk, lstOfInd]
    if cows[int(goal)-1]==milk:
        getmilk=True
    

    for i in range(len(paths)):
        if paths[i][1]==goal:
            lstOfInd.append(i)
            return travelpath(start, paths[i][0], milk, destination, getmilk, lstOfInd)

# print(travelpath(friends[1][0], friends[1][1], friends[1][2]))


ans=""
count=0
for i in range(len(friends)):
    answer = travelpath(friends[i][0], friends[i][1], friends[i][2])
    if(answer!=None):

        print(answer[5])
        ans+=str(int(answer[4]==True))
        
    else:
        if i==0:
            print(i)
        count+=1
    # print(answer)
    # ans+=str(int(answer[4]==True))

    # print(answer)

print(ans)

test="0110001011111110110111111111111011111111101111111111011111011011111111001111001110110111101100101111011101101111111111101110001001110111101101101111110111001100100011111111111111111111111111111111111101001111110110101011111110011111111111111110111111110001001011100111111111111011101101111001101110100110110111101000101111110111011101011111111010001101101011011111111011111111111010111111111101011111111101011111111111011110111011100111111111111111111110111111110111011100"
print(len(test))
print(count)