n,m,k = input().split()
n=int(n)
m=int(m)
k=int(k)

emails=[]
for i in range(k):
    temp=input().split()
    for j in range(len(temp)):
        temp[j]=int(temp[j])

    emails.append(temp)

# print(emails)
# emails=[[5, 1, 10], [1, 3, 4], [2, 3, 9], [1, 4, 1]]
emails.sort(key = lambda x:x[1])
# emails = sorted(emails, key = lambda x:(x[1], x[0]))

# print(emails)
answers=[-1 for _ in range(n)]
i=0
j=1
while i<len(emails):
    
    max=float("-inf")
    prof=-1
    while True and i<len(emails):
        
        if emails[i][1]==j:
            # if emails[i][0]==prof:
            #     max+=emails[i][2]

            
            if emails[i][2]>max:
                max=emails[i][2]
                prof=emails[i][0]
                
            i+=1
        else:
            break
        

    answers[j-1]=prof
    j+=1

# if len(answers)!=n:
#     answers.append(-1)
x=""
for i in range(len(answers)):
    x+=str(answers[i])+" "

x=x[0:-1]
print(x)