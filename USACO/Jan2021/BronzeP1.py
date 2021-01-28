alpha=input()
heard=input()

count=0
while len(heard)!=0:

    for i in range(len(alpha)):
        if len(heard)==0:
            break

        if alpha[i]==heard[0]:

            heard=heard[1:]


    count+=1

print(count)