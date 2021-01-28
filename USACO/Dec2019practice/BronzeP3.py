f=open("lineup.in", "r")
names=['Beatrice ', 'Belinda ', 'Bella ', 'Bessie ', 'Betsy ', 'Blue ', 'Buttercup ', 'Sue ']
lines=f.read().split("\n")[1:-1]
f.close()
pairs=[]
for i in range(len(lines)):
    words=lines[i].split(" ")
    pairs.append([words[0], words[-1]])

# print(pairs)

answer=[]
permuts=[]
def permutations(start, tail=''):
    if len(start) == 0:
        permuts.append(tail.split())
    else:
        for i in range(len(start)):
            permutations(start[:i] + start[i+1:], tail + start[i])

permutations(names)

def search():
    for i in range(len(permuts)):
        score=0

        for k in range(0, len(permuts[i])-1, 1):
            for j in range(len(pairs)):
                for l in range(len(pairs[j])):
                    if permuts[i][k]==pairs[j][l]:
                        if permuts[i][k+1]==pairs[j][1-l]:
                            score+=1

        # print(score)

        if score==len(pairs):

            return permuts[i]

correct=search()
f=open("lineup.out", "a")
for i in range(7):
    f.write(correct[i] +"\n")

f.write(correct[7])
f.close()
