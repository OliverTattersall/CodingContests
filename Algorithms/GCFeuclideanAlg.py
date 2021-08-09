
def gcd(a,b):
    if a==0 or b==0:
        return a+b
    
    r=a%b
    a=b
    b=r
    return gcd(a,b)

print(gcd(1000034384, 12934212))