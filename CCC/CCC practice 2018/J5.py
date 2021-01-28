N=int(input())

pages=[]
for i in range(N):
    pages.append(input().split())



shortestpath=float("inf")

visitpages=[False for i in range(N)]




def followpath(n, count):

    global shortestpath

    n=int(n)

    if visitpages[n-1]==False:
        visitpages[n-1]=True


        if len(pages[n-1])>1:

            for i in range(int(pages[n-1][0])):

                followpath(pages[n-1][i+1], count+1)

        else:

            if count+1<shortestpath:
                shortestpath=count+1

    


for i in range(int(pages[0][0])):

    followpath(int(pages[0][i+1]), 1)
    
visitpages[0]=True


# print(visitpages)


answer=True
for i in range(N):
    if visitpages[i]==False:
        answer=False
        break

if answer==True:
    print("Y")

else:

    print("N")


print(shortestpath)