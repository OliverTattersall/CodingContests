totalattractions, maxattractions=input().split(" ")
attractions=input().split(" ")
totalattractions=int(totalattractions)
maxattractions=int(maxattractions)
offdays=totalattractions%maxattractions
for i in range(totalattractions):
    attractions[i] = int(attractions[i])


def solve(ats, off):
    # print(ats, off)
    if len(ats)==maxattractions or len(ats)==offdays:
        return max(ats)
    
    incl =max(ats[0:maxattractions])+solve(ats[maxattractions:], off)
    if off:
        offday = float("-inf")
    else:
        offday = max(ats[0:offdays]) + solve(ats[offdays:], True)

    print(incl, offday)
    return max(incl, offday)

if offdays==0:
    answer = solve(attractions, True)
else:
    answer = solve(attractions, False)

print(answer)