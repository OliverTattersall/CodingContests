aro = input()

conv = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

sum = int(aro[-2])*conv[aro[-1]]

for i in range(0, len(aro)-2, 2):
    if conv[aro[i+3]]>conv[aro[i+1]]:
        sum-=conv[aro[i+1]]*int(aro[i])

    else:
        sum+=conv[aro[i+1]]*int(aro[i])

print(sum)