n=int(input())

ans = ""
num=0
if n<10**5:
    for i in range(n):
        ans+="9 "
    ans=ans[0:-1]
    num=n

else:
    j=1
    while 2**j<n:
        j+=1

    if 2**j - 1 ==n:
        for i in range(j):
            ans+=str(i)+" "
        ans=ans[0:-1]
        num=j
    else:
        ans="Sad Chris"




if num!=0:
    print(num)
print(ans)