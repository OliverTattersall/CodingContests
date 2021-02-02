j, w, h = input().split()
j = int(j)
w = int(w)
h = int(h)
game = []

for i in range(h):
    game.append(list(input()))

# print(game)

end = False

for i in range(w):
    for j in range(h):
        if game[j][i]=="L":
            start=i
            height=j
count = start+1
index = start
# height = len(game)-2
while end!=True:
    index+=1
    count+=1

    if game[height][index]=="G":
        count = -1
        break
    if game[height][index]=="@":
        made = False
        for i in range(1, j):
            if height-i>=0:
                if game[height-i][index]==".":
                    made = True
                    break
            else:
                end = True

                break
        if made:
            count+=1
            index+=1
        else:
            end=True
            break


print(count)

    