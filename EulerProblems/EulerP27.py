def SieveOfEratosthenes(n): 
    primes=[]
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    # print(len(prime))
    p = 2
    #goes until √n at which point there would be no more composite numbers left True
    while (p * p <= n): 
        #print(prime[p])
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            #print(p)
            primes.append(p)
    #print(primes)
    #print(len(primes))
    return primes



p = set(SieveOfEratosthenes(1000000))
# print(p)
pair=()
max=0
for i in range(-999, 1000, 1):
    for j in range(-999, 1000, 1):
        count=0
        if abs(j) in p:

            
            f = lambda x: x**2 +i*x+j

            k=0
            n= f(0)
            while abs(n) in p:
                count+=1
                k+=1
                n=f(k)
            if count>max:
                pair=(i,j)

        if (abs(i)==67 and abs(j)==971) or (abs(j)==67 and abs(i)==971):
            print(count, i, j)

print(pair)