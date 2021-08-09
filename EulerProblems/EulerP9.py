'''
finds pythagorean triple where a + b +c =n and returns abc
'''

def triplet(n):
    for a in range(1, n):
        for b in range(1, n):
            c = 1000-a-b
            if c**2 == a**2+b**2:
                return a*b*c

print(triplet(1000))