needle=input()
haystack=input()+" "

possibilities=set([])


needleLetters={}

for i in range(len(needle)):
    needleLetters[needle[i]]=needleLetters.get(needle[i], 0)+1

temp={}
for j in range(len(needle)):
    temp[haystack[j]]=temp.get(haystack[j], 0)+1
if temp==needleLetters:
    possibilities.add(haystack[0:len(needle)])


for i in range(1, len(haystack)-len(needle)):
    
    item=haystack[i:i+len(needle)]

    temp[haystack[i-1]]=temp[haystack[i-1]]-1
    if temp[haystack[i-1]]==0:
        del temp[haystack[i-1]]

    temp[item[-1]]=temp.get(item[-1], 0)+1
    # for j in range(len(item)):
    #     temp[item[j]]=temp.get(item[j], 0)+1
    
    if temp==needleLetters:
        possibilities.add(item)

    # print(i, haystack[i])
    # print(temp)



# for i in range(len(haystack)-len(needle)+1):

#     temp={}
#     item=haystack[i:i+len(needle)]

#     for j in range(len(item)):
#         temp[item[j]]=temp.get(item[j], 0)+1

#     if temp==needleLetters:
#         possibilities.add(item)





print(len(possibilities))

