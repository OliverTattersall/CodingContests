
for _ in range(10):
    first = input().split()
    r = int(first[0])
    t = int(first[1])
    rules = {}
    rules2={}
    original = first[2]
    for i in range(r):
        line = input().split()
        temp = {}
        for i in range(len(line[1])):
            temp[line[1][i]] = temp.get(line[1][i], 0)+1
        rules[line[0]] = temp
        rules2[line[0]] = line[1]
    # print(rules, rules2)
    front = original[0]
    end = original[-1]

    letters={}

    for i in range(len(original)):
        letters[original[i]] = letters.get(original[i], 0)+1

    # print(letters)
    for i in range(t):
        front = rules2[front][0]
        end = rules2[end][-1]
        keys = list(letters.keys())
        # print(letters)
        count={}
        for j in keys:
            keys2 = list(rules[j].keys())
            # print(j, keys2, rules)

            for k in keys2:
                # print()
                count[k] = count.get(k, 0)+(rules[j][k])*letters[j]
        # print(count)
        letters = count.copy()

    sum = 0
    # print(keys)
    for i in range(len(keys)):
        sum+=letters[keys[i]]
    # print(letters, sum)
    print(front+end, sum)