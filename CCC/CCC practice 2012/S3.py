

n = int(input())

readings ={}

for i in range(n):
    temp = int(input())
    readings[temp] = readings.get(temp, 0)+1

freqs = {}
keys = list(readings.keys())
# print(readings)

for i in keys:
    # print(freqs)
    if readings[i] not in freqs:
        freqs[readings[i]] = (i,)
    else:
        freqs[readings[i]]=freqs[readings[i]] +(i,) 

# print(freqs)

keys2 = list(freqs.keys())
keys2.sort()
# print(keys2[-1], keys2[-2])

first = 0
second = 0

if len(freqs[keys2[-1]])==1 and len(freqs[keys2[-2]])==1:
    first = list(freqs[keys2[-1]])[0]
    second = list(freqs[keys2[-2]])[0]

elif len(freqs[keys2[-1]])==1 and len(freqs[keys2[-2]])!=1:
    first = list(freqs[keys2[-1]])[0]
    vals = list(freqs[keys2[-2]])
    second=vals[0]
    for i in range(len(vals)):
        if abs(first-vals[i])>abs(first-second):
            second=vals[i]
elif len(freqs[keys2[-1]])!=1:
    vals = list(freqs[keys2[-1]])
    first = max(vals)
    second = min(vals)
    


print(abs(first-second))