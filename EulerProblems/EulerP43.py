
count = 0
primes = [2,3,5,7,11,13,17]
nums = set([0,1,2,3,4,5,6,7,8,9])

# for i in range(10**9, 10**10, 1):
#     if len(set(list(str(i))))==10 and str(i)[0]!=0:
#         temp = str(i)
#         flag = True
#         for j in range(7):
#             if int(temp[j+1:j+4])%primes[j]!=0:
#                 flag=False
#                 break
#         if flag:
#             count+=1
# print(count)


div17 = []

for i in range(1,1000,1):
    temp =list(str(i))
    if len(set(temp))==len(str(i)):
        if i%17==0:
            div17.append(i)
        # print()
print(len(div17))

div13 = []

for i in range(len(div17)):
    if div17[i]//100==0:
        temp = '0'+str(div17[i])
    else:
        temp = str(div17[i])


    temp2 = nums.copy()
    # print(temp2, temp)
    temp2.remove(int(temp[0]))
    temp2.remove(int(temp[1]))
    temp2.remove(int(temp[2]))
    
    temp2 = list(temp2)
    for j in range(7):
        temp3 = int(str(temp2[j])+temp[0:2])
        if temp3%13==0:
            
            div13.append((temp3, div17[i], set(temp2)))

print(len(div13))


div11 = []

for i in range(len(div13)):
    # if len(div13[i])!=3:
    #     print(div13[i])
    if div13[i][0]//100==0:
        temp = '0'+str(div13[i][0])
    else:
        temp = str(div13[i][0])

    temp2 = div13[i][-1].copy()
    
    temp2.remove(int(temp[0]))

    temp2 = list(temp2)
    for j in range(6):
        temp3 = int(str(temp2[j])+temp[0:2])
        if temp3%11==0:
            temp4 = (temp3, )+div13[i][0:2]+(set(temp2, ), )

            div11.append(temp4)
print(len(div11))

div7=[]

for i in range(len(div11)):
    # if len(div13[i])!=3:
    #     print(div13[i])
    if div11[i][0]//100==0:
        temp = '0'+str(div11[i][0])
    else:
        temp = str(div11[i][0])

    temp2 = div11[i][-1].copy()
    
    temp2.remove(int(temp[0]))

    temp2 = list(temp2)
    for j in range(len(temp2)):
        temp3 = int(str(temp2[j])+temp[0:2])
        if temp3%7==0:
            temp4 = (temp3, )+div11[i][0:3]+(set(temp2, ), )

            div7.append(temp4)

print(len(div7))

div5 = []

for i in range(len(div7)):
    # if len(div13[i])!=3:
    #     print(div13[i])
    if div7[i][0]//100==0:
        temp = '0'+str(div7[i][0])
    else:
        temp = str(div7[i][0])

    temp2 = div7[i][-1].copy()
    
    temp2.remove(int(temp[0]))

    temp2 = list(temp2)
    for j in range(len(temp2)):
        temp3 = int(str(temp2[j])+temp[0:2])
        if temp3%5==0:
            temp4 = (temp3, )+div7[i][0:4]+(set(temp2, ), )

            div5.append(temp4)

print(len(div5))

div3 = []

for i in range(len(div5)):
    # if len(div13[i])!=3:
    #     print(div13[i])
    if div5[i][0]//100==0:
        temp = '0'+str(div5[i][0])
    else:
        temp = str(div5[i][0])

    temp2 = div5[i][-1].copy()
    
    temp2.remove(int(temp[0]))

    temp2 = list(temp2)
    for j in range(len(temp2)):
        temp3 = int(str(temp2[j])+temp[0:2])
        if temp3%3==0:
            temp4 = (temp3, )+div5[i][0:5]+(set(temp2, ), )

            div3.append(temp4)

print(len(div3))

div2 = []
for i in range(len(div3)):
    # if len(div13[i])!=3:
    #     print(div13[i])
    if div3[i][0]//100==0:
        temp = '0'+str(div3[i][0])
    else:
        temp = str(div3[i][0])

    temp2 = div3[i][-1].copy()
    
    temp2.remove(int(temp[0]))

    temp2 = list(temp2)
    for j in range(len(temp2)):
        temp3 = int(str(temp2[j])+temp[0:2])
        if temp3%2==0:
            temp4 = (temp3, )+div3[i][0:6]+(set(temp2, ), )

            div2.append(temp4)

print(len(div2))
sum = 0
for i in range(len(div2)):
    if div2[i][0]//100==0:
        temp = '0'+str(div2[i][0])
    else:
        temp = str(div2[i][0])
    
    temp2 = div2[i][-1].copy()
    temp2.remove(int(temp[0]))
    temp2 = list(temp2)[0]
    end = str(temp2)
    for j in range(len(div2[i])-1):
        if div2[i][j]//100==0:
            temp3 = '0'+str(div2[i][j])
        else:
            temp3 = str(div2[i][j])
        end+=temp3[0]
        if j==len(div2[i])-2:
            end+=temp3[1:]
    # end+=str(div2[i][-2])
    print(end)
    sum+=int(end)

print(sum)