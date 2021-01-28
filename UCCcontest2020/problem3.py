haybales=int(input())
tractornum=int(input())
tractors=input().split(" ")
areawidth=int(input())
areastring=input()

largestgap=0
trips=0
treeloc=[]

# numtrees=areastring.count("1")
for i in range(areawidth):
    if areastring[i]=="1":
        treeloc.append(i)
# print(treeloc)

for i in range(len(treeloc)-1):
    if((treeloc[i+1]-(treeloc[i]+1))>largestgap):
        largestgap=(treeloc[i+1]-(treeloc[i]+1))

# print(largestgap)
for i in range(tractornum-1, -1, -1):
    if int(tractors[i])<=largestgap:
        rest=haybales%int(tractors[i])
        
        trips+=(haybales-rest)/int(tractors[i])+1
        print(trips)
        break
print("\n")
print(int(trips))
        