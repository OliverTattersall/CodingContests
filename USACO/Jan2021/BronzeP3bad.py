def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):

                yield perm[:i] + elements[0:1] + perm[i:]

n=int(input())
cheights=input().split()
bheights=input().split()

for i in range(n):
    cheights[i]=int(cheights[i])
    bheights[i]=int(bheights[i])

cheights.sort()
groups=0
options=list(all_perms(cheights))
for i in range(len(options)):
    temp=list(options[i])
    test=True
    for j in range(n):
            
        if temp[j]>bheights[j]:
            test=False
    if test:
        groups+=1

print(groups)
        
                