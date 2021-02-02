test=int(input())
answers=[]
for i in range(test):
    lines=int(input())
    commands=[]
    functions=[]
    functioncommands=[]
    for j in range(lines):
        commands.append(input().split(" "))
    score=0
    j=0
    while j<lines:
        if commands[j][0]=="FUN":
            functions.append(commands[j][1])
            for k in range(j, lines, 1):
                if commands[k][0]=="END":
                    adder=[]
                    for l in range(j+1, k-j,1):
                        adder.append(commands[j+l])
                    functioncommands.append(adder)
                    j+=(k-j)
                    break

        elif commands[j][0]=="ADD":
            score=score+int(commands[j][1])
        elif commands[j][0]=="MULT":
            score=score*int(commands[j][1])
        elif commands[j][0]=="SUB":
            score=score-int(commands[j][1])
        elif commands[j][0]=="CALL":
            for k in range(len(functions)):
                if commands[j][1]==functions[k]:
                    for l in range(len(functioncommands[k])):
                        if(functioncommands[k][l][0]=="ADD"):
                            score=score+int(functioncommands[k][l][1])
                        elif(functioncommands[k][l][0]=="MULT"):
                            score=score*int(functioncommands[k][l][1])
                        elif(functioncommands[k][l][0]=="SUB"):
                            score=score-int(functioncommands[k][l][1])
        j+=1
    print(score%1000000007)
    # answers.append(score%1000000007)

# for i in range(len(answers)):
#     print(answers[i])