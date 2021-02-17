n = int(input())

first=input().split()
second = input().split()

pairs={}
answer = "good"
for i in range(n):
    first[i] = first[i].lower()
    second[i] = second[i].lower()
    if first[i] not in pairs:
        if second[i] not in pairs:
            pairs[first[i]] = second[i]
            pairs[second[i]] = first[i]
        else:
            answer = "bad"
            break
    elif second[i] not in pairs:
        if first[i] not in pairs:
            pairs[first[i]] = second[i]
            pairs[second[i]] = first[i]
        else:
            answer = "bad"
            break
    else:
        if pairs[first[i]] != second[i]:
            answer="bad"
            break
        if pairs[second[i]] != first[i]:
            answer="bad"
            break

print(answer)
