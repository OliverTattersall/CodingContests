f=open("whereami.in", "r")
line=f.read().split("\n")[1]
f.close()
# print(line)
answer=0
for i in range(1, len(line)):
    dct={}
    for j in range(0, len(line)-i+1):
        dct[line[j:j+i]]=dct.get(line[j:j+i], 0)+1
        # print(line[j:j+i])
    # print(dct)
    # print(max(dct.values()))
    if max(dct.values())==1:
        answer=i
        break

# print(answer)

f=open("whereami.out", "w")
f.write(str(answer))
f.close()
