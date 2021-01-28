t=int(input())
answers=[]
ones="2"
tens=["4", "9"]
hundreds=[192, 442, 692, 942]


# def reduce(n, count):
#     if n==0:
#         return count
#     else:
#         return reduce(n//10, count+1)

for i in range(t):

    k=int(input())
    if k<1000:
        for j in range(4):
            if k<=hundreds[j]:
                answers.append(hundreds[j])
                break

    else:
        k=str(k)
        extra=k[-3:]

        for j in range(4):
            if int(extra)<=hundreds[j]:
                answers.append(k[:-3]+str(hundreds[j]))
                break



for i in range(t):
    print(answers[i])


