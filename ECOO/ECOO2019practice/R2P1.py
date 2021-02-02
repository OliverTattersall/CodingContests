answers=[]
for _ in range(10):
    num = int(input())
    emails = set([])
    for i in range(num):
        temp = input().lower().split("@")
        front = temp[0]
        back = temp[1]
        j = 0
        while True:
            if j<len(front):
                if front[j]==".":
                    front = front[0:j]+front[j+1:]
                if j<len(front):
                    if front[j]=="+":
                        front = front[0:j]
                        break
            else:
                break
            j+=1
            

        # while front.count(".")>0:
        #     front = front.replace(".", "")
        # if "+" in front:
        #     j = front.index("+")
        #     front = front[:j]
        emails.add(front+"@"+back)




    answers.append(len(list(emails)))

print(answers)