## not done

k,n = map(int, input().split())

rounds= []
for i in range(n):
    temp = list(map(int, input().split()))
    rounds.append(temp)

scores={i:0 for i in range(1, k+1)}
ranks={i:0 for i in range(1,k+1)}
worst={i:0 for i in range(1,k+1)}
for i in range(n):
    temp={}
    rev={}
    for j in range(k):
        scores[j+1]+=rounds[i][j]
        temp[scores[j+1]]= temp.get(scores[j+1], 0)+1
        temp = {key:temp[key] for key in sorted(temp)[::-1]}
        rev[scores[j+1]] = rev.get(scores[j+1], ())+(j+1, )
    count=1
    # print(rev)
    for key in temp.keys():
        for j in range(len(rev[key])):
            ranks[rev[key][j]]=count
            if ranks[rev[key][j]]>worst[rev[key][j]]:
                worst[rev[key][j]] = count
        count+= temp[key]

# print('\n')  
# print(worst)
# print(scores)
# print(ranks)

result = "Yodeller {} is the TopYodeller: score {}, worst rank {}"
for i in range(1, k+1):
    if ranks[i]==1:
        print(result.format(i, scores[i], worst[i]))
