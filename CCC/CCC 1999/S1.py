high = ['jack', 'queen', 'king', 'ace']
A = 0
B = 0
count=0
score=0
player=''
end = []

for i in range(52):
    temp = input().rstrip()

    if temp in high:
        
        x = high.index(temp)
        # print(temp, x)
        count = 0
        score = 0
        count = x
        score = x+1
        if i %2 ==0:
            player = 'A'
        else:
            player = 'B'


    else:
        if count!=0:
            count=count -1
        elif count==0 and player!='':
            # print('\n',i)
            endstr = 'Player {p} scores {n} point(s).'.format(p=player, n=score)
            end.append(endstr)
            if player=='A':
                A+=score
            else:
                B+=score
            player = ''

endstr1 = 'Player A: {n} point(s).'.format(n=A)
endstr2 = 'Player B: {n} point(s).'.format(n=B)
end.append(endstr1)
end.append(endstr2)

for j in range(len(end)):
    print(end[j])


