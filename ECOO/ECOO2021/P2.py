dna = input()

vowel={"A"}
con={"C","T","G"}

words=[]

i=0
while len(dna)!=0:
    if i+1==len(dna):
        words.append(dna[0:i+1])
        dna=dna[i+1:]
        continue

    if dna[i] in vowel:
        if dna[i+1] in vowel:
            words.append(dna[0:i+1])
            dna=dna[i+1:]
            i=0
            continue
            
    if dna[i] in con:
        if dna[i+1] in con:
            words.append(dna[0:i+1])
            dna=dna[i+1:]
            i=0
            continue

    i+=1

# print(words)

ans=""
for i in range(len(words)):
    ans+=words[i]+" "

ans=ans[0:-1]
print(ans)

