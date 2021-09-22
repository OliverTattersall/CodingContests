terms = set([])

for a in range(2, 101,1):
    for b in range(2, 101, 1):
        terms.add(a**b)
print(len(terms))