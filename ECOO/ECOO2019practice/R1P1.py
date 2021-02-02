answers = []

for k in range(10):
    first = input().split()
    clean = int(first[0])
    m = int(first[1])
    d = int(first[2])

    events=[]

    second = input().split()


    for i in range(m):
        events.append(int(second[i]))
    events.sort()


    add = clean
    laundry = 0
    index = 0
    # print(events)
    for i in range(1, d):
        if clean == 0:
            laundry+=1
            clean+=add
        clean = clean - 1

        if index<len(events):
            if i == events[index]:
                clean+=1
                add+=1
                index+=1

                while index<len(events) and i == events[index]:
                    clean+=1
                    add+=1
                    index+=1

        # print(clean, i, laundry)

    # print(laundry, events)

    answers.append(laundry)

# print("\n")
print(answers)