st = int(input())

inter=int(input())

send = int(input())

saw = 0
for i in range(3): 
    st+=inter
    if st>=send:
        saw=st
        break

if saw==0:
    saw="Who knows..."

print(saw)